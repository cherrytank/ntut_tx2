# Jetson TX2 detectNet Lab

本課程使用 Jetson TX2 完成：

1. GPIO LED 控制
2. Webcam 即時影像
3. AI 物件偵測
4. 偵測到 person 時 LED 亮

## 課程流程

```text
0:00-0:10  git pull、說明安裝流程
0:10-0:35  學生安裝 jetson-inference
0:35-0:45  檢查環境
0:45-1:00  GPIO LED 閃爍
1:00-1:10  Webcam 顯示
1:10-1:25  detectNet 物件偵測
1:25-1:30  detectNet + GPIO、加分挑戰
```

## 下載程式

```bash
git clone <你的 repo>
cd tx2-detectnet-lab
git pull
```

## 安裝 jetson-inference

學生在自己的 Jetson TX2 上執行：

```bash
bash setup/install_jetson_inference.sh
```

安裝需要網路，也可能需要輸入 Jetson 的 sudo 密碼。

如果安裝過程出現模型選單，至少選：

```text
SSD-Mobilenet-v2
```

這個模型適合教學，辨識類別包含 `person`、`bottle`、`chair` 等常見物件。

注意：第一次安裝和編譯會花比較久。若網路或 TX2 速度較慢，建議老師先讓學生在課前或上課一開始執行安裝。

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

## AI 物件偵測

```bash
bash run_detectnet.sh
```

## AI + GPIO

```bash
bash run_detectnet_gpio.sh
```

## 離開程式

在視窗中按 `q`，或在 terminal 按 `Ctrl + C`。

## 學生任務

必做：

```text
任務 1：讓 LED 閃爍
任務 2：開啟 Webcam
任務 3：跑出 AI 物件偵測畫面
任務 4：讓模型偵測 person
```

加分：

```text
任務 5：把 THRESHOLD 從 0.5 改成 0.7
任務 6：把 TARGET_CLASS 改成 bottle
任務 7：偵測到 person 時 LED 亮
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
