# Jetson TX2 YOLOv4-tiny Lab

使用 Jetson TX2 完成：

1. GPIO LED 控制
2. Webcam 即時影像
3. OpenCV DNN + YOLOv4-tiny 物件偵測
4. 偵測到 person 時 LED 亮


## 課程流程

```text
0:00-0:10  git pull、下載 YOLOv4-tiny 模型
0:10-0:20  檢查環境
0:20-0:40  GPIO LED 閃爍
0:40-0:55  Webcam 顯示
0:55-1:15  YOLOv4-tiny 物件偵測
1:15-1:30  YOLOv4-tiny + GPIO、加分挑戰
```

## 下載程式

```bash
git clone https://github.com/cherrytank/ntut_tx2.git
```

## 下載 YOLOv4-tiny 模型

```bash
bash setup/download_models.sh
```

下載後 `models/` 內應該會有：

```text
yolov4-tiny.cfg
yolov4-tiny.weights
coco.names
```

## 檢查環境

```bash
bash setup/check_env.sh
```

## GPIO LED

```bash
bash run_gpio.sh
```

## Webcam

```bash
bash run_webcam.sh
```

## YOLOv4-tiny 圖片偵測

```bash
bash run_yolo_image.sh path/to/image.jpg
```

偵測結果會存到：

```text
outputs/yolov4_tiny_result.jpg
```

## YOLOv4-tiny Webcam 偵測

```bash
bash run_yolo_webcam.sh
```

## YOLOv4-tiny + GPIO

```bash
bash run_yolo_gpio.sh
```

## 離開程式

在視窗中按 `q`，或在 terminal 按 `Ctrl + C`。

## 任務

```text
任務 1：下載 YOLOv4-tiny 模型
任務 2：讓 LED 閃爍
任務 3：開啟 Webcam
任務 4：跑出 YOLOv4-tiny 物件偵測畫面
任務 5：讓模型偵測 person
```

```text
任務 6：把 CONF_THRESHOLD 從 0.5 改成 0.7
任務 7：把 TARGET_CLASS 改成 bottle
任務 8：偵測到 person 時 LED 亮
任務 9：如果 TX2 跑太慢，把 INPUT_WIDTH / INPUT_HEIGHT 改成 320
```

## 硬體接線

```text
Jetson TX2 Pin 12  ---- 電阻 ---- LED 長腳
Jetson TX2 GND     ------------ LED 短腳
```

材料：

```text
LED x1
220Ω 或 330Ω 電阻 x1
杜邦線
麵包板
USB Webcam
```

更多接線說明請看 [docs/wiring_gpio_led.md](docs/wiring_gpio_led.md)。
常見問題請看 [docs/troubleshooting.md](docs/troubleshooting.md)。
