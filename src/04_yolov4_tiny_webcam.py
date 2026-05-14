import time

import cv2
import numpy as np


MODEL_CFG = "models/yolov4-tiny.cfg"
MODEL_WEIGHTS = "models/yolov4-tiny.weights"
CLASS_NAMES = "models/coco.names"

CAMERA_ID = 0
CONF_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
INPUT_WIDTH = 416
INPUT_HEIGHT = 416


def get_output_layers(net):
    layer_names = net.getLayerNames()
    unconnected_layers = net.getUnconnectedOutLayers()
    layer_ids = np.array(unconnected_layers).flatten()

    return [layer_names[int(i) - 1] for i in layer_ids]


with open(CLASS_NAMES, "r", encoding="utf-8") as f:
    classes = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNetFromDarknet(MODEL_CFG, MODEL_WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

output_layers = get_output_layers(net)

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("Cannot open camera")
    raise SystemExit(1)

prev_time = time.time()

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

        if len(indexes) > 0:
            for i in np.array(indexes).flatten():
                x, y, w, h = boxes[i]
                label = classes[class_ids[i]]
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

        now = time.time()
        fps = 1.0 / max(now - prev_time, 0.001)
        prev_time = now

        cv2.putText(
            frame,
            f"YOLOv4-tiny FPS: {fps:.1f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
        )

        cv2.imshow("YOLOv4-tiny Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Stop")

finally:
    cap.release()
    cv2.destroyAllWindows()
