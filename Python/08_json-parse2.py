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
orig = "Вашингтон"
dest = "Москва"
key = "aDuDw1nPuPKZPXgyZIeqa1gPZh7x5mM3"
# Собираем ссылку
url = main_api + urllib.parse.urlencode({
    "key": key,
    "from": orig,
    "to": dest
    })

# Выводим url для браузера
print("\n" + "URL: " + url + "\n")

# Переменная куда запишем ответ запроса в формате json
json_data = requests.get(url).json()

json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API status: " + str(json_status) + " = A succesful route call. \n")
else:
    print("API status messages" + str(json_data["info"]["messages"]) + "\n")
