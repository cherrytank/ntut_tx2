#!/bin/bash

echo "========== TX2 detectNet Lab Check =========="

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
echo "[5] jetson_inference / jetson_utils"
python3 - << 'EOF'
try:
    import jetson_inference
    import jetson_utils
    print("jetson-inference OK")
except Exception as e:
    print("jetson-inference FAIL:", e)
EOF

echo ""
echo "========== Done =========="
