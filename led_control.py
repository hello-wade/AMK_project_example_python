import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

while True:
    GPIO.output(31, True)
    print("led on")
    time.sleep(2)

    GPIO.output(31, False)
    print("led off")
    time.sleep(2)
