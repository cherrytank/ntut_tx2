# Troubleshooting

## 找不到 camera

先執行：

```bash
ls /dev/video*
```

如果沒有看到 `/dev/video0`，請檢查：

1. USB Webcam 是否已插好。
2. Webcam 是否被其他程式佔用。
3. 重新插拔 Webcam 後再執行一次。

如果 camera 不是 `/dev/video0`，請修改：

```python
INPUT = "/dev/video0"
```

或：

```python
CAMERA_ID = 0
```

## OpenCV 視窗沒有出現

請確認目前是在 Jetson TX2 桌面環境中執行，而不是純 SSH terminal。

如果透過 SSH 操作，通常無法直接顯示 `cv2.imshow()` 視窗。

## Jetson.GPIO 匯入失敗

執行：

```bash
bash setup/check_env.sh
```

如果看到 `Jetson.GPIO FAIL`，請確認 Jetson.GPIO 已安裝，或請老師協助檢查 JetPack 環境。

## jetson-inference 匯入失敗

如果看到：

```text
jetson-inference FAIL
```

代表 `jetson_inference` 或 `jetson_utils` 還不能被 Python 找到。

請老師先確認每台 TX2 已完成：

```bash
cd jetson-inference/build
sudo make install
sudo ldconfig
```

## detectNet 第一次啟動很慢

第一次啟動模型時，TensorRT 可能需要建立最佳化 engine，所以會比較久。

同一台機器之後再次執行通常會快很多。

## 沒有偵測到 person

可以先調低信心門檻：

```python
THRESHOLD = 0.3
```

也可以確認：

1. 人是否在鏡頭畫面中。
2. 光線是否足夠。
3. Webcam 是否對焦正常。

## LED 一直亮或一直不亮

請確認：

1. `TARGET_CLASS = "person"` 是否拼字正確。
2. terminal 是否有印出 `person`。
3. LED 腳位是否接在 Pin 12。
4. GND 是否接好。

也可以先跑：

```bash
bash run_gpio.sh
```

確認 LED 硬體接線沒問題，再回到 AI + GPIO 程式。
