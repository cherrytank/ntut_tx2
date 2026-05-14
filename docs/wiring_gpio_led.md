# GPIO LED 接線

本課程使用 Jetson TX2 的實體腳位編號，也就是 `GPIO.BOARD` 模式。

## 材料

```text
LED x1
220Ω 或 330Ω 電阻 x1
杜邦線
麵包板
USB Webcam
```

## 接線

```text
Jetson TX2 Pin 12  ---- 電阻 ---- LED 長腳
Jetson TX2 GND     ------------ LED 短腳
```

LED 長腳通常是正極，短腳通常是負極。

## 檢查重點

1. LED 一定要串接電阻。
2. 程式中的 `LED_PIN = 12` 對應 Jetson TX2 實體腳位 Pin 12。
3. GND 要接到 Jetson TX2 的 GND 腳位。
4. 如果 LED 沒亮，可以先將 LED 長短腳方向對調後再測一次。

## 執行 GPIO 測試

```bash
bash run_gpio.sh
```

看到 terminal 交替顯示 `LED ON`、`LED OFF` 時，LED 應該會同步閃爍。
