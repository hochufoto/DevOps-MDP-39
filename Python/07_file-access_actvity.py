# Запускаем безконечный цикл
while True:
# Создаем новый item и заполняем его новыми данными
    newitem = input("Enter device name: ")
# Создаем условие для выхода по команде exit
    if newitem == "exit":
# Выводим сообщение о завершении программы
        print("All Done")
# Прерываем цикл после команды exit
        break
# Открываем файл devices.txt в режиме добавления данных
    with open("devices.txt", "a") as file:
# Записываем содержимое newitem в файл с новой строки
        file.write(newitem + "\n")
# Закрываем файл
file.close()
