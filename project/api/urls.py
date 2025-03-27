from django.urls import path
from . import views

# Logic starts here with user making a request
# Matches incoming URLs with view functions

urlpatterns = [
    path('cocktails/', views.cocktail_page, name='cocktail page'),
    path('cocktails/letter/', views.cocktail_letter_view, name='cocktail letter view'),
    path('cocktails/ingredient/', views.cocktail_by_ingredient, name = "cocktail by ingredients"),
    # path('path that triggers the view', view function that is called if url matches)
]