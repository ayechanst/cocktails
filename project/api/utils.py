import requests

def get_cocktail_by_name(name):
    url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('drinks', [])
    return []

def get_cocktail_by_letter(letter):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('drinks', [])
        trimmed_data = [
            {
                'id': drink.get('idDrink'),
                'name': drink.get('strDrink'),
                'instructions': drink.get('strInstructions'),
                'glass': drink.get('strGlass'),
                'ingredient1': drink.get('strIngredient1'),
                'ingredient2': drink.get('strIngredient2'),
                'ingredient3': drink.get('strIngredient3'),
                'ingredient4': drink.get('strIngredient4'),
                'ingredient5': drink.get('strIngredient5'),
                'ingredient6': drink.get('strIngredient6'),
                'ingredient7': drink.get('strIngredient7'),
            }
            for drink in data if drink
        ]
        return trimmed_data
    return []

