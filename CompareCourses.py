import requests

API_KEY = ''
URL = 'https://api.exchangeratesapi.io/v1/latest? access_key = {API_KEY}'
currencies = []
baseCurrency

def getCurrencyData(URL, API_KEY):
    rawData = requests.get(url = URL)
    json = rawData.json()
    return json

def calculateNewBaseCurrency(currencies, newBaseCurrency):
    for currency in currencies.keys:
        currencies[currency] /= currencies[newBaseCurrency]
    return currencies

def compareCurrencies(baseCurrency, otherCurrencies):
    return

def table(headers, contents):
    return