# main.py
import cProfile
from device import Device
from home_manager import HomeManager

# Создаем несколько устройств
device1 = Device(1, "Лампа")
device2 = Device(2, "Термостат")

# Создаем менеджер умного дома
home_manager = HomeManager()

# Добавляем устройства в систему
home_manager.add_device(device1)
home_manager.add_device(device2)

# Выводим список устройств
print("Список устройств:")
for device in home_manager.get_device_list():
    print(f"ID: {device.device_id}, Имя: {device.name}, Статус: {device.status}")

# Изменяем статус устройства
device1.change_status("включено")

# Выводим обновленный список устройств
print("\nОбновленный список устройств:")
for device in home_manager.get_device_list():
    print(f"ID: {device.device_id}, Имя: {device.name}, Статус: {device.status}")

# Удаляем устройство
home_manager.remove_device(device2)

# Выводим список устройств после удаления
print("\nСписок устройств после удаления:")
for device in home_manager.get_device_list():
    print(f"ID: {device.device_id}, Имя: {device.name}, Статус: {device.status}")

#Демонстрация изменений в потребляемости 
cProfile.run("home_manager.add_device(device1)", sort='tottime')
cProfile.run("home_manager.generate_device(device2)", sort='tottime')

