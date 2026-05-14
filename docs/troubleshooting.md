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
CAMERA_ID = 0
```

## OpenCV 視窗沒有出現

請確認目前是在 Jetson TX2 桌面環境中執行，而不是純 SSH terminal。

如果透過 SSH 操作，通常無法直接顯示 `cv2.imshow()` 視窗。

## OpenCV 匯入失敗

執行：

```bash
bash setup/check_env.sh
```

如果看到 `OpenCV FAIL`，請確認 Jetson TX2 的 Python 環境中有安裝 OpenCV。

## DNN module 顯示 False

如果檢查結果是：

```text
DNN module: False
```

代表這個 OpenCV 沒有 `cv2.dnn`，無法使用 OpenCV DNN 載入 YOLO。

這種情況不建議現場重編 OpenCV，請改用備案，例如 YOLOv3-tiny 或 OpenCV 顏色偵測。

## 模型檔案 missing

如果看到：

```text
cfg missing
weights missing
names missing
```

請執行：

```bash
bash setup/download_models.sh
```

下載後再檢查：

```bash
bash setup/check_env.sh
```

## YOLOv4-tiny load FAIL

如果錯誤訊息包含：

```text
Unsupported activation
Parsing error
readNetFromDarknet failed
```

可能是 TX2 上的 OpenCV 版本太舊，讀不了 YOLOv4-tiny 的 Darknet config。

課堂上不要現場重編 OpenCV，直接切到備案比較穩。

## 如果 TX2 跑太慢

把程式中的：

```python
INPUT_WIDTH = 416
INPUT_HEIGHT = 416
```

改成：

```python
INPUT_WIDTH = 320
INPUT_HEIGHT = 320
```

速度會好一點，但準確率會下降。

## 沒有偵測到 person

可以先調低信心門檻：

```python
CONF_THRESHOLD = 0.3
```

也可以確認：

1. 人是否在鏡頭畫面中。
2. 光線是否足夠。
3. Webcam 是否對焦正常。
4. `models/coco.names` 裡的類別名稱是否是 `person`。

## LED 一直亮或一直不亮

請確認：

1. `TARGET_CLASS = "person"` 是否拼字正確。
2. terminal 或畫面是否有出現 `person`。
3. LED 腳位是否接在 Pin 12。
4. GND 是否接好。

也可以先跑：

```bash
bash run_gpio.sh
```

確認 LED 硬體接線沒問題，再回到 YOLO + GPIO 程式。
