import RPi.GPIO as GPIO
from time import *

class Buzzer:
	def __init__(self):
		self.pin = 12
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)
		self.p = GPIO.PWM(self.pin, 300)

	def beep(self, pin):
		GPIO.setwarnings(False)
		GPIO.output(pin, True)
		self.p.start(0)
		self.p.ChangeDutyCycle(100)
		self.p.ChangeFrequency(100)
		sleep(0.5)
		p.stop()

		GPIO.output(pin, False)
		sleep(2)

		GPIO.cleanup()

Buzzer = Buzzer()
Buzzer.beep(12)

