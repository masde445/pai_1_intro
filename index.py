import requests

def pobierz(sciezka)
    dane = requests.get(sciezka).text
    return dane

xd = pobierz('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
print(xd)
