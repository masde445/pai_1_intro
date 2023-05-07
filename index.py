import requests


def pobierz(sciezka)
    dane = requests.get(sciezka).text
    if dane.status_code > 299:
        return 0
    else:
        dane = dane.text
        return dane

def post(sciezka)
    x = {"name":"Natalia"}
    dane = requests.post(sciezka, json=x)
    return dane.text

xd = pobierz('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
print(xd)
xd2 = post('https://httpbin.org/post')
print(xd2)
