# device.py
class Device:
    #Функции без побочных эффектов 15 - 17
    def __init__(self, device_id, name, status="выключено"): #Методы изменены так, чтобы они возвращали новые объекты, не изменяя текущие.
        self.device_id = device_id
        self.name = name
        self.status = status

    def change_status(self, new_status):
        return Device(self.device_id, self.name, new_status)
