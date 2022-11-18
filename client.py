import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Geralt", "views": 23, "likes": 78},
        {"name": "Yennefer", "views": 1200, "likes": 37},
        {"name": "Jaskier", "views": 180, "likes": 10}]

for i in range(len(data)):
    response = requests.put(
        BASE + "video/1" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
