# home_manager.py
import json
import logging
from device import Device

class HomeManager:
    def __init__(self, devices=None):
        #Использование неизменяемых структур данных 15 - 17
        self.devices = devices if devices else [] #Вместо изменяемого списка self.devices в HomeManager, создадается новый список при каждом изменении и возращаем его, чтобы сохранить неизменяемость.
        self.logger = logging.getLogger("HomeManager")
        logging.basicConfig(level=logging.INFO)

    #Повышение эффективности 18 - 20
    def generate_device(self, device):
        new_devices = [*self.devices, device] #Использование генераторов для создания списков: до new_devices = self.devices + [device]
        self.logger.info(f"Добавлено устройство: {device.name}")
        return HomeManager(new_devices)

    #Функции без побочных эффектов 15 - 17
    def add_device(self, device): #Методы изменены так, чтобы они возвращали новые объекты, не изменяя текущие.
        new_devices = self.devices + [device] #использование генераторов для создания списков: после new_devices = [*self.devices, device]
        self.logger.info(f"Добавлено устройство: {device.name}")
        return HomeManager(new_devices)
    
    #По сути generate_device и add_device выполняют один и тот же функционал. Но в 1 функции происходит использование генераторов для создания списков

    #Функции без побочных эффектов 15 - 17
    def remove_device(self, device): #Методы изменены так, чтобы они возвращали новые объекты, не изменяя текущие.
        new_devices = [d for d in self.devices if d != device]
        self.logger.info(f"Удалено устройство: {device.name}")
        return HomeManager(new_devices)

    def get_device_list(self):
        return self.devices

    def save_state(self, filename):
        state = {
            "devices": [
                {"id": device.device_id, "name": device.name, "status": device.status}
                for device in self.devices
            ]
        }
        with open(filename, "w") as file:
            json.dump(state, file)
            self.logger.info(f"Состояние системы сохранено в файл: {filename}")

    def load_state(self, filename):
        with open(filename, "r") as file:
            state = json.load(file)
            new_devices = [
                Device(device["id"], device["name"])
                for device in state["devices"]
            ]
            self.logger.info(f"Состояние системы загружено из файла: {filename}")
            return HomeManager(new_devices)
        
