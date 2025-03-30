import threading
from selenium import webdriver
from time import sleep
from modules.sensormodel import SensorModel
from modules.sensorcontroller import SensorController
from modules.drivercontroller import DriverController
import json


if __name__ == "__main__":
    
    sensor = SensorModel()
    driver_model = webdriver.Chrome()
    driver_controller = DriverController(driver_model)

    while (1):
        SensorController.readSerial(sensor)
        sleep(0.1)
        driver_controller.run(sensor.code)
