#!/bin/bash
cd "$(dirname "$0")"
python3 src/03_yolov4_tiny_image.py "$@"
