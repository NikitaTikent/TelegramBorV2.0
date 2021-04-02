import urllib.request
from lxml.html import fromstring  # подключаем библиотеку lxml

def ParseAll():
    # Парсинг курса валют
    response = urllib.request.urlopen('https://coinmarketcap.com/currencies/ethereum/').read()
    page = fromstring(response)  # делаем из нашей строки объект для манипулирования страницей
    nameSite = page.xpath(
        '//*[@id="__next"]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div')  # получаем все элементы с переданным xpath
    XRP = nameSite[0].text

    response = urllib.request.urlopen('https://orenburg.vbr.ru/banki/kurs-valut/prodaja-usd/').read()
    page = fromstring(response)  # делаем из нашей строки объект для манипулирования страницей
    nameSite = page.xpath('//*[@id="value_0"]')  # получаем все элементы с переданным xpath
    Dol = nameSite[0].text
    return XRP, Dol