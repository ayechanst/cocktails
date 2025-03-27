import requests

def get_cocktail_by_name(name):
    url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('drinks', [])
    return []


