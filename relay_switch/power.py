import time
from RPi import GPIO


class Power:
    """
    Works well with for both low-level trigger and high-level trigger.
    """
    def __init__(self, channel):
        self.channel = channel

    def on(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(self.channel, GPIO.LOW)

        GPIO.cleanup(self.channel)

    def off(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.channel, GPIO.LOW)

        GPIO.cleanup(self.channel)
