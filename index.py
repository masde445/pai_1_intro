import requests
from requests.exceptions import Timeout
import time

def pobierz(sciezka):
    dane = requests.get(sciezka)
    if dane.status_code > 299:
        return 0
    else:
        dane = dane.text
        return dane

def post(sciezka):
    x = {"name":"Natalia"}
    dane = requests.post(sciezka, json=x)
    return dane.text

def timeout_http(sciezka, max_retries, retry_t):
    retries = 0
    while retries < max_retries:
        try:
            y = requests.get(sciezka, timeout=1)
            return y.text
        except Timeout:
            print("request timed out")
            time.sleep(retry_t[retries])
            retries += 1
    return "too many requests has been made"

def exponential_numbers(limit):
    retries_t = []
    x = 1
    while x <= limit:
        retries_t.append(x)
        x *= 2
    return retries_t

xd = pobierz('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
print(xd)
xd2 = post('https://httpbin.org/post')
print(xd2)
expo = exponential_numbers(10)
xd3 = timeout_http('https://httpbin.org/delay/2', 4, expo)
print(xd3)
