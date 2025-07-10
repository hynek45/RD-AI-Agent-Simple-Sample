import requests

def fetch_bitcoin_usd():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()["bitcoin"]["usd"]
