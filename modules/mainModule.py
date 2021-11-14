from subprocess import PIPE
from bmp280 import BMP280

#! BPM280 Sensor
try:
    from smbus2 import SMBus

except ImportError:
    from smbus import SMBus

#! Buzzer Module
import RPi.GPIO as GPIO
from time import sleep

#! NEO6M Module
from datetime import *
import serial

#! HDC1080 Sensor
import sys
from modules import SDL_Pi_HDC1080

class BMP:
    def __init__(self):
        # Initialize the BMP280
        self.bus = SMBus(1)
        self.bmp280 = BMP280(i2c_dev=self.bus)

    def temp(self, decimal):
        temperature = round(self.bmp280.get_temperature(), decimal)
        return temperature

    def press(self, decimal):
        pressure = round(self.bmp280.get_pressure(), decimal)
        return pressure

    def alt(self, decimal):
        baseline_values = []
        baseline_size = 100

        # Calibration with 100 sampling
        for i in range(baseline_size):
            baseline_values.append(round(self.bmp280.get_pressure(), 4))

        baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])
        altitude = round(self.bmp280.get_altitude(qnh=baseline), decimal)
        return altitude

class Buzzer:
	GPIO.setmode(GPIO.BOARD)
	
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		self.p = GPIO.PWM(self.pin, 300)

	def beep(self):
		GPIO.setwarnings(False)
		GPIO.output(self.pin, True)
		self.p.start(0)
		self.p.ChangeDutyCycle(100)
		self.p.ChangeFrequency(100)
		sleep(0.5)
		self.p.stop()

		GPIO.output(self.pin, False)
		sleep(2)

		GPIO.cleanup()


mport = '/dev/ttyAMA0' #choose your com port on which you connected your neo 6m GPS


class NEO:
    def decode(self,coord):
        l = list(coord)
        for i in range(0,len(l)-1):
            if l[i] == "." :
                break
        base = l[0:i-2]
        degi = l[i-2:i]
        degd = l[i+1:]
        baseint = int("".join(base))
        degiint = int("".join(degi))
        degdint = float("".join(degd))
        degdint = degdint / (10**len(degd))
        degs = degiint + degdint
        full = float(baseint) + (degs/60)

        return full

    def paser(self,data):
        if data[0:6] == "$GPGGA":
            s = data.split(",")
            if s[7] == '0' or s[7]=='00':
                print ("no satellite data available")
                return
            time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
            lat = self.decode(s[2])
            lon = self.decode(s[4])
            return lat,lon

    def GPS(self):
        ser = serial.Serial(mport,9600,timeout = 2)

        dat = ser.readline().decode()
        mylat,mylon = self.paser(dat)

        return mylat, mylon


class HDC:
	def __init__(self):
		sys.path.append('./modules/SDL_Pi_HDC1080_Python3')
		self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

	def temp(self, decimal):
		temperature = round(self.hdc1080.readTemperature(), decimal)
		return temperature

	def hum(self, decimal):
		humidity = round(self.hdc1080.readHumidity(), decimal)
		return humidity
