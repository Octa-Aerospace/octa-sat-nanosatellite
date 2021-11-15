from time import sleep
from .modules.mainModule import NEO, HDC, BMP, Buzzer

class Main:
    def __init__(self):
        self.NEO = NEO()
        self.HDC = HDC()
        self.BMP = BMP()
        self.Buzzer = Buzzer()

    def NEO_read(self):
        return self.NEO.read()

    def HDC_read(self):
        return self.HDC.read(decimal=2) #* temp, hum
    
    def BMP_read(self):
        return self.BMP.read(decimal=2) #* temp, press, alt

    def Buzzer_beep(self):
        self.Buzzer.beep_on()
        sleep(0.5) #! if we put this sleep, that will affect the module's reads
        self.Buzzer.beep_off() 
        sleep(2) #! same the above

    def start(self):
        while True:
            self.NEO_read()
            self.HDC_read()
            self.BMP_read()
            self.Buzzer_beep()
            sleep(1)

App = Main()
App.start()