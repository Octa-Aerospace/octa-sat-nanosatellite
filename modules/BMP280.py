from subprocess import PIPE, Popen
from bmp280 import BMP280

try:
    from smbus2 import SMBus

except ImportError:
    from smbus import SMBus


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

    def read(self, decimal):
        return self.temp(decimal), self.press(decimal), self.alt(decimal)
