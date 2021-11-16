from time import sleep
from datetime import datetime as dt
from modules.mainModule import NEO, HDC, BMP, Buzzer
from modules.transceiver import LORA

class OctaSat:
    def __init__(self):
        self.NEO = NEO()
        self.HDC = HDC()
        self.BMP = BMP()
        self.Buzzer = Buzzer()
        self.LORA = LORA()

    def NEO_read(self):
        return self.NEO.read() #* lat, lon

    def HDC_read(self):
        return self.HDC.read(decimal=2) #* temp, hum
    
    def BMP_read(self):
        return self.BMP.read(decimal=2) #* temp, press, alt

    def Buzzer_beep(self):
        self.Buzzer.beep_on()
        sleep(0.5) #! if we put this sleep, that will affect the module's reads
        self.Buzzer.beep_off() 
        sleep(2) #! same the above

    def LORA_send(self, data):
        self.LORA.send(data)

    def Time(self):
        now = dt.datetime.now()
        return now.strftime('%d/%m, %H:%M:%S')

    def start(self):
        latitude, longitude = self.NEO_read()
        hdc_temperature, humidity = self.HDC_read()
        bmp_temperature, pressure, altitude = self.BMP_read()
        self.Buzzer_beep() #* just beep
        
        data = {
            'latitude': latitude,
            'longitude': longitude,
            'hdc_temperature': hdc_temperature,
            'bmp_temperature': bmp_temperature,
            'humidity': humidity,
            'pressure': pressure,
            'altitude': altitude,
            'time': self.Time()
        }

        payload = self.LORA.prepare_payload(data) #* formating payload ready to send
        self.LORA_send(payload) #* send payload

        sleep(1)