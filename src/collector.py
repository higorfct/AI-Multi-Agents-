import requests

def fetch_bcb_data(code):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados/ultimos/1?formato=json"
    response = requests.get(url)
    return response.json()[0]['valor']

def collect_macro_data():
    return {
        "pib": fetch_bcb_data(4380),         # PIB
        "inflacao": fetch_bcb_data(433),     # IPCA
        "cambio": fetch_bcb_data(1),         # Dólar comercial
        "juros": fetch_bcb_data(4189)        # Selic
    }
