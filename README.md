# Jetson TX2 detectNet Lab

使用 Jetson TX2 完成：
1. GPIO LED 控制
2. Webcam 即時影像
3. AI 物件偵測
4. 偵測到 person 時 LED 亮

## 下載程式

```bash
git clone https://github.com/cherrytank/ntut_tx2.git

```

## 安裝 jetson-inference


```bash
bash setup/install_jetson_inference.sh
```

安裝需要網路，也可能需要輸入 Jetson 的 sudo 密碼。

如果安裝過程出現模型選單，至少選：

```text
SSD-Mobilenet-v2
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

## 任務


```text
任務 1：讓 LED 閃爍
任務 2：開啟 Webcam
任務 3：跑出 AI 物件偵測畫面
任務 4：讓模型偵測 person
```


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
