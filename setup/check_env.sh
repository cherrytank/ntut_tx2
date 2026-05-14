#!/bin/bash

echo "========== TX2 YOLOv4-tiny Lab Check =========="

echo ""
echo "[1] Python"
python3 --version

echo ""
echo "[2] Camera"
ls /dev/video* 2>/dev/null || echo "No camera found"

echo ""
echo "[3] OpenCV"
python3 - << 'EOF'
try:
    import cv2
    print("OpenCV OK:", cv2.__version__)
    print("DNN module:", hasattr(cv2, "dnn"))
except Exception as e:
    print("OpenCV FAIL:", e)
EOF

echo ""
echo "[4] Jetson.GPIO"
python3 - << 'EOF'
try:
    import Jetson.GPIO as GPIO
    print("Jetson.GPIO OK")
except Exception as e:
    print("Jetson.GPIO FAIL:", e)
EOF

echo ""
echo "[5] Model files"
test -s models/yolov4-tiny.cfg && echo "cfg OK" || echo "cfg missing"
test -s models/yolov4-tiny.weights && echo "weights OK" || echo "weights missing"
test -s models/coco.names && echo "names OK" || echo "names missing"

echo ""
echo "[6] OpenCV DNN load test"
python3 - << 'EOF'
try:
    import os
    import cv2

    cfg = "models/yolov4-tiny.cfg"
    weights = "models/yolov4-tiny.weights"

    if not os.path.exists(cfg) or not os.path.exists(weights):
        print("YOLOv4-tiny load SKIP: model files missing")
        print("Run: bash setup/download_models.sh")
    else:
        cv2.dnn.readNetFromDarknet(cfg, weights)
        print("YOLOv4-tiny load OK")
except Exception as e:
    print("YOLOv4-tiny load FAIL:", e)
    print("If this is an Unsupported activation or parsing error, use the YOLOv3-tiny fallback.")
EOF

echo ""
echo "========== Done =========="
