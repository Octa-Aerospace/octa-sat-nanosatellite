import RPi.GPIO as GPIO
from time import *

#! Origin Class
# class Buzzer:
# 	GPIO.setmode(GPIO.BOARD)
	
# 	def __init__(self, pin):
# 		self.pin = pin
# 		GPIO.setup(self.pin, GPIO.OUT)
# 		self.p = GPIO.PWM(self.pin, 300)

# 	def beep(self):
# 		GPIO.setwarnings(False)
# 		GPIO.output(self.pin, True)
# 		self.p.start(0)
# 		self.p.ChangeDutyCycle(100)
# 		self.p.ChangeFrequency(100)
# 		sleep(0.5)
# 		self.p.stop()

# 		GPIO.output(self.pin, False)
# 		sleep(2)

# 		GPIO.cleanup()

# Buzzer = Buzzer(12)
# Buzzer.beep()

class Buzzer:
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)

	def beep_on(self):
		GPIO.output(self.pin, True)

	def beep_off(self):
		GPIO.output(self.pin, False)

#* This is an use example of the class
# Buzzer = Buzzer(12)
# Buzzer.beep_on()
# sleep(0.5)
# Buzzer.beep_off()
# sleep(2)

