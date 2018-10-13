import RPi.GPIO as GPIO


class fan_util():
    stat = False
    pin = 2
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, False)

    def set_stat(self, value):
        self.stat = value
        self.refresh()

    def get_stat(self):
        return GPIO.input(self.pin)

    def refresh(self):
        if self.stat is False:
            self.fan_off()
        else:
            self.fan_on()

    def fan_on(self):
        GPIO.output(self.pin, True)

    def fan_off(self):
        GPIO.output(self.pin, False)

    def invert(self):
        GPIO.output(self.pin, not GPIO.input(self.pin))

    def cleanup(self):
        GPIO.cleanup()
