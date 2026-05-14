# Jetson TX2 YOLOv4-tiny Lab

使用 Jetson TX2 完成：

1. GPIO LED 控制
2. Webcam 即時影像
3. OpenCV DNN + YOLOv4-tiny 物件偵測
4. 偵測到 person 時 LED 亮

## 下載程式

```bash
git clone https://github.com/cherrytank/ntut_tx2.git
```

## 下載 YOLOv4-tiny 模型

```bash
bash setup/download_models.sh
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