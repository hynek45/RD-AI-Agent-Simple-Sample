import requests

def usd_to_czk():
    url = "https://open.er-api.com/v6/latest/USD"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()["rates"]["CZK"]
