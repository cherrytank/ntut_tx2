import Jetson.GPIO as GPIO
from jetson_inference import detectNet
from jetson_utils import videoOutput, videoSource


LED_PIN = 12

INPUT = "/dev/video0"
OUTPUT = "display://0"
NETWORK = "ssd-mobilenet-v2"
THRESHOLD = 0.5
TARGET_CLASS = "person"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

net = detectNet(NETWORK, threshold=THRESHOLD)
camera = videoSource(INPUT)
display = videoOutput(OUTPUT)

try:
    while display.IsStreaming():
        img = camera.Capture()

        if img is None:
            continue

        detections = net.Detect(img)

        found_target = False

        for detection in detections:
            class_name = net.GetClassDesc(detection.ClassID)
            confidence = detection.Confidence

            print(class_name, confidence)

            if class_name == TARGET_CLASS:
                found_target = True

        if found_target:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        display.Render(img)
        display.SetStatus("detectNet + GPIO | {:.0f} FPS".format(net.GetNetworkFPS()))

except KeyboardInterrupt:
    print("Stop")

finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
