from modules.commands import commands

class DriverController():
    
    def __init__(self, model):
        self.model = model
    
    def run(self, code):

        try:
            action = commands[code]
            print(action)
            metodo = getattr(self, action)
            
            if callable(metodo):
                return metodo()
            else:
                return None
        except KeyError:
            return None
    
    def netflix(self):
        self.model.get('https://netflix.com')
    
    def prime_video(self):
        self.model.get('https://primevideo.com')
    
    def vol_up(self):
        print("Volume UP")
    
    def vol_down(self):
        print("Volume DOWN")
