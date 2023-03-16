# Создаем пустой список devices
devices=[]
# Создаем переменную содержимое которого читаем из файла devices.txt
file = open("./Python/devices.txt","r")
# с помощью for проходимся по всему файлу и заносим содержимое file в служебную переменную item
for item in file:
# удаляем пустые абзацы
    item=item.strip()
# добавляем элементы в список devices
    devices.append(item)
# Закрываем объязательно файл!!!
file.close()
# Выводим содержимое списка devices
print(devices)
