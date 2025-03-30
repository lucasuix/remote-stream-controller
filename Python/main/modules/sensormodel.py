import serial
import json
from modules.model import Model

class SensorModel(Model):
    
    __slots__ = Model.__slots__ + ["system", "port", "code", "baud_rate", "microSerial"]
    __excludes__ = ["microSerial"] # Dados que não são escritos para o JSON
    
    def __init__(self):
        super().__init__(config_file="sensor.json") # Chama o construtor da superclasse para o arquivo de configuracao sensor.json
        self.setAttrsFromConfig() # Recupera os dados e os coloca como atributos da instância
        self.microSerial = serial.Serial(self.port, self.baud_rate)
    
    def readSerial(self):
        if (self.microSerial.inWaiting() > 0):
            self.code = self.microSerial.readline()
