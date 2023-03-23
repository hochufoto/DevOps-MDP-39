# Мой GitHub
# https://github.com/hochufoto/DevOps-MDP-39.git

# Импортируем библиотеку urllib.parse
import urllib.parse
# Импортируем библиотеку requests для выполнения GET запроса
import requests
# Определяем переменные
# main_api ссылка для запроса
# orig откуда едем
# dest куда едем
# key api key
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "aDuDw1nPuPKZPXgyZIeqa1gPZh7x5mM3"
unit = "k"
locale = "ru_RU"

# Запускаем цикл
while True:
# Функция ввода даных с клавиатуры
    orig = input("Начальная точка: ")
# Добовляем команду для выхода из программы
    if orig == "quit" or orig == "q" or orig == "exit":
        break
    dest = input("Пункт назначения: ")
# Добовляем команду для выхода из программы
    if dest == "quit" or dest == "q" or dest == "exit":
        break

# Собираем ссылку
    url = main_api + urllib.parse.urlencode({
        "key": key,
        "from": orig,
        "to": dest,
        "unit": unit,
        "locale": locale
        })

# Выводим url для браузера
    print("\n" + "URL: " + url + "\n")

# Переменная куда запишем ответ запроса в формате json
    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API status: " + str(json_status) + " = A succesful route call. \n")
        print("Направления от " + (orig) + " до " + (dest))
        print("Продолжительность поездки:  " + (json_data["route"]["formattedTime"]))
        print("Расстояние: " + str("{:.2f}".format((json_data["route"]["distance"]))) + " Км")
        print("=" * 70 + "\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format(each["distance"]) + " Км)"))
        print("=" * 70 + "\n")
    else:
        print("API status messages" + str(json_data["info"]["messages"]) + "\n")
