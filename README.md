# 🍸 Cocktail Finder 🍹

An API Client built using Python and Django. All thanks to [TheCocktailDB](https://www.thecocktaildb.com/)

- Improved data filtering (find drinks by **letters** or **ingredients**)
- Removed bloat information from drink recipes
- Easy to use website

### Easy to read recipes

Take a look at recipes available to make with Kool-Aid:

```json
[
  {
    "name": "Kool First Aid",
    "glass": "Shot glass",
    "ingredient1": "151 proof rum",
    "ingredient2": "Kool-Aid",
    "instructions": "Add Kool Aid to a double shot glass, and top with rum. Slam and shoot."
  },
  {
    "name": "Kool-Aid Slammer",
    "glass": "Shot glass",
    "ingredient1": "Kool-Aid",
    "ingredient2": "Vodka",
    "instructions": "Fill half the shot glass with the kool-aid first. Then put a paper towel over the top of the glass and slowly pour in the vodka. If you do it right, you should be able to see that the two liquids are separated, with the vodka on top. Now slam it! The last thing you'll taste is the kool-aid."
  },
  {
    "name": "Zippy's Revenge",
    "glass": "Old-fashioned glass",
    "ingredient1": "Amaretto",
    "ingredient2": "Rum",
    "ingredient3": "Kool-Aid",
    "instructions": "Mix Kool-Aid to taste then add Rum and ammaretto. shake well to disolve the sugar in the Kool-Aid... serve cold"
  }
]
```

### Minimum simple UI

![Home Page](/pics/home.png)

### Seach by letter

Just click on a letter and get all the cocktail recipes from TheCocktailDB

![Search by letter](/pics/seach-by-letter.png)

### Search by ingredient

Want a cocktail but don't have the ingredients for your go-to's? Try clicking on what
you have in the kitchen and liquor cabinet and seeing what you can make!

![Search by ingredient](/pics/search-by-ingredient.png)
