import cv2
import Jetson.GPIO as GPIO
import numpy as np


MODEL_CFG = "models/yolov4-tiny.cfg"
MODEL_WEIGHTS = "models/yolov4-tiny.weights"
CLASS_NAMES = "models/coco.names"

CAMERA_ID = 0
LED_PIN = 12

CONF_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
INPUT_WIDTH = 320
INPUT_HEIGHT = 320
TARGET_CLASS = "person"


def get_output_layers(net):
    layer_names = net.getLayerNames()
    unconnected_layers = net.getUnconnectedOutLayers()
    layer_ids = np.array(unconnected_layers).flatten()

    return [layer_names[int(i) - 1] for i in layer_ids]


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

with open(CLASS_NAMES, "r", encoding="utf-8") as f:
    classes = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNetFromDarknet(MODEL_CFG, MODEL_WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

output_layers = get_output_layers(net)

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("Cannot open camera")
    GPIO.cleanup()
    raise SystemExit(1)

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Cannot receive frame")
            break

        height, width = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(
            frame,
            1 / 255.0,
            (INPUT_WIDTH, INPUT_HEIGHT),
            swapRB=True,
            crop=False,
        )

        net.setInput(blob)
        outputs = net.forward(output_layers)

        boxes = []
        confidences = []
        class_ids = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = int(np.argmax(scores))
                confidence = float(scores[class_id])

                if confidence > CONF_THRESHOLD:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(confidence)
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(
            boxes,
            confidences,
            CONF_THRESHOLD,
            NMS_THRESHOLD,
        )

        found_target = False

        if len(indexes) > 0:
            for i in np.array(indexes).flatten():
                label = classes[class_ids[i]]

                if label == TARGET_CLASS:
                    found_target = True

                x, y, w, h = boxes[i]
                confidence = confidences[i]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{label} {confidence:.2f}",
                    (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )

        if found_target:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        cv2.imshow("YOLOv4-tiny + GPIO", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Stop")

finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
