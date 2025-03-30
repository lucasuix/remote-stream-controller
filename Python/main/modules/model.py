import json

class Model:
    
    __slots__ = ["data_path", "config_file", "config_path"]
    
    def __init__(self, data_path="data/json/", config_file=""):
        self.data_path = data_path
        self.config_file = config_file
        self.config_path = data_path + config_file
        
    def setAttrsFromConfig(self):
        data = self.readConfig()
        for key, value in data.items():
            setattr(self, key, value)
    
    def readConfig(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f'Arquivo {self.config_file} não encontrado em {self.data_path}.')
    
    def writeToConfig(self, data, excludes):
        for key, value in excludes:
            data.pop(key, None)
        try:
            with open(self.config_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print(f'Arquivo {self.config_file} não encontrado em {self.data_folder}.')
    
    def saveAttrs(self):
        config_data = {attr: getattr(self,attr) for attr in self.__slots__}
        self.writeToConfig(config_data)
        
    def setAttrTo(self, parameter, value):
        setattr(self, parameter, value)
        
    def setAttrList(self, parameter_dict):
        for attr in self.__slots__:
            setattr(self, attr, parameter_dict[attr])
