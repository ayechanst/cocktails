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
                'name': drink.get('strDrink'),
                'glass': drink.get('strGlass'),
                **{f'ingredient{i}': drink.get(f'strIngredient{i}')
                    for i in range(1, 9) if drink.get(f'strIngredient{i}')
                   },
                'instructions': drink.get('strInstructions'),
            }
            for drink in data if drink
        ]
        return trimmed_data
    return []

# Add for faster ingredient search

# def get_cocktail_by_ingredient(ingredient):
#     url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()

    # cocktail_array = []


def get_cocktail_by_ingredient(ingredient):
    cocktail_array = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
        response = requests.get(url)
        if response.status_code == 200:
            drink_group = response.json().get('drinks', [])
            if drink_group:
                for drink in drink_group:
                    for i in range(1, 9):
                        drink_ingredient = drink.get(f'strIngredient{i}')
                        if drink_ingredient == ingredient:
                            trimmed_data = {
                                'name': drink.get('strDrink'),
                                'glass': drink.get('strGlass'),
                                **{f'ingredient{i}': drink.get(f'strIngredient{i}')
                                    for i in range(1, 9) if drink.get(f'strIngredient{i}')
                                },
                                'instructions': drink.get('strInstructions'),
                            }
                            cocktail_array.append(trimmed_data)
                            break
    return cocktail_array

def get_all_ingredients():
    ingredient_set = set() 
    for letter in "abcdefghijklmnopqrstuvwxyz":
        url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
        response = requests.get(url)
        # response = await fetch_data(url)
        if response.status_code == 200:
            data = response.json().get('drinks', [])
            # data = response.get('drinks', [])
            if data:
                for drink in data:
                    for i in range(1, 9):
                        ingredient = drink.get(f'strIngredient{i}')
                        if ingredient:
                            ingredient_set.add(ingredient)
    return sorted(ingredient_set)







