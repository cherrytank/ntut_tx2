#!/bin/bash
set -e

INSTALL_DIR="${JETSON_INFERENCE_DIR:-$HOME/jetson-inference}"
REPO_URL="https://github.com/dusty-nv/jetson-inference"

echo "========== Install jetson-inference =========="
echo "Install path: $INSTALL_DIR"
echo ""

echo "[1] Install basic packages"
sudo apt-get update
sudo apt-get install -y git cmake libpython3-dev python3-numpy

echo ""
echo "[2] Clone or update jetson-inference"
if [ -d "$INSTALL_DIR/.git" ]; then
    echo "Repository already exists. Updating..."
    git -C "$INSTALL_DIR" pull --ff-only
    git -C "$INSTALL_DIR" submodule update --init --recursive
else
    git clone --recursive "$REPO_URL" "$INSTALL_DIR"
fi

echo ""
echo "[3] Configure build"
mkdir -p "$INSTALL_DIR/build"
cd "$INSTALL_DIR/build"

echo ""
echo "If a model selection window appears, select at least:"
echo "  SSD-Mobilenet-v2"
echo ""

cmake ../

echo ""
echo "[4] Build"
make -j"$(nproc)"

echo ""
echo "[5] Install"
sudo make install
sudo ldconfig

echo ""
echo "[6] Verify Python import"
python3 - << 'EOF'
import jetson_inference
import jetson_utils

print("jetson-inference OK")
EOF

echo ""
echo "========== Install complete =========="
