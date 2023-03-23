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
orig = "Нальчик"
dest = "Москва"
key = "aDuDw1nPuPKZPXgyZIeqa1gPZh7x5mM3"
# Собираем ссылку
url = main_api + urllib.parse.urlencode({
    "key": key,
    "from": orig,
    "to": dest
    })
# Переменная куда запишем ответ запроса в формате json
json_data = requests.get(url).json()
# Выводим результат на экран.
print(json_data)
# Выводим url для браузера
print("\n" + "URL: " + url + "\n")
