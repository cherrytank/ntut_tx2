#!/bin/bash
set -e

MODEL_DIR="models"
CFG_URL="https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg"
WEIGHTS_URL="https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"
NAMES_URL="https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names"

download_file() {
    local url="$1"
    local output="$2"

    if [ -s "$output" ]; then
        echo "$(basename "$output") already exists"
        return
    fi

    if command -v wget >/dev/null 2>&1; then
        wget -O "$output" "$url"
    elif command -v curl >/dev/null 2>&1; then
        curl -L "$url" -o "$output"
    else
        echo "Please install wget or curl first."
        exit 1
    fi
}

echo "========== Download YOLOv4-tiny Models =========="

mkdir -p "$MODEL_DIR"

download_file "$CFG_URL" "$MODEL_DIR/yolov4-tiny.cfg"
download_file "$WEIGHTS_URL" "$MODEL_DIR/yolov4-tiny.weights"
download_file "$NAMES_URL" "$MODEL_DIR/coco.names"

echo ""
echo "Model files:"
ls -lh "$MODEL_DIR/yolov4-tiny.cfg" "$MODEL_DIR/yolov4-tiny.weights" "$MODEL_DIR/coco.names"

echo ""
echo "========== Done =========="
