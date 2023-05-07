import requests

def pobierz(sciezka)
    dane = requests.get(sciezka).text
    if dane.status_code > 299:
        return 0
    else:
        dane = dane.text
        return dane

xd = pobierz('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
print(xd)
