import serial
import json
from modules.sensormodel import SensorModel

class SensorController:
    
    @staticmethod
    def readSerial(model):
        model.readSerial()
    
    @staticmethod
    def readConfig(model):
        model.readConfig()
    
    @staticmethod
    def writeToConfig(model, data, excludes):
        model.writeToConfig(data, excludes)
    
    @staticmethod
    def saveAttrs(model):
        model.saveAttrs()
    
    @staticmethod
    def setAttrTo(model, attribute, value):
        str_keys = ["data_path", "config_path", "config_file",
                    "system", "port"]
        num_keys = ["code", "baud_rate"]
        
        if(attribute in str_keys and isstring(value)):
            model.saveAttrs(attribute, value)
        elif(attribute in num_keys and isnumeric(value)):
            model.saveAttrs(attribute, value)
        else:
            print(f'Items (Atribute:{attribute}, Value: {value} ) not a valid attribute or value.')
    
    @staticmethod
    def setAttrDict(model, parameter_dict):
        for key, value in parameter_dict.items():
            SensorController.setAttrTo(self, key, value)
