import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TOUCH_PIN = 12

GPIO.setup(TOUCH_PIN, GPIO.IN)

try:
    while True:
        touch_state = GPIO.input(TOUCH_PIN)
        if touch_state == GPIO.LOW:
            print("Touch sensor is not touched.")
        else:
            print("Touch sensor is touched!")
        
except KeyboardInterrupt:
    GPIO.cleanup()
