from jetson_inference import detectNet
from jetson_utils import videoOutput, videoSource


INPUT = "/dev/video0"
OUTPUT = "display://0"
NETWORK = "ssd-mobilenet-v2"
THRESHOLD = 0.5

net = detectNet(NETWORK, threshold=THRESHOLD)
camera = videoSource(INPUT)
display = videoOutput(OUTPUT)

try:
    while display.IsStreaming():
        img = camera.Capture()

        if img is None:
            continue

        detections = net.Detect(img)

        for detection in detections:
            class_name = net.GetClassDesc(detection.ClassID)
            confidence = detection.Confidence
            print(class_name, confidence)

        display.Render(img)
        display.SetStatus("detectNet | {:.0f} FPS".format(net.GetNetworkFPS()))

except KeyboardInterrupt:
    print("Stop")
