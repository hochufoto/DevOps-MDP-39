# Запускаем программу в безконечном цикле
while True:
# Создаем переменную х значение которого будем вводить сами
    x=input("Enter a number to count to: ")
# Создаем условие, что при вводе q или quit цикл останавливается функцией break
# и работа программы завершается 
    if x == "q" or x == "quit":
        break
# ковертируем введеное значение в integer
    x=int(x)
# Создаем переменную у равную 1
    y=1
# Запускаем цикл который будет выполняться безконечно
    while True:
# Выводим текущее значение
        print(y)
# Прибовляем к у 1 за каждый цикл
        y=y+1
# Добавляем условие при котором произойдет остановка цикла через функцию break     
        if y>x:
            break
