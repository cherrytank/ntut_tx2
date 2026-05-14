import time

import Jetson.GPIO as GPIO


LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(0.5)

        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stop")

finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
