from django.urls import path
from . import views

# They all start with api/ before the rest of the shit
urlpatterns = [
    path('cocktails/', views.cocktail_view, name='single cocktail view'),
    path('letter/cocktails/', views.cocktail_letter_view, name='cocktail letter view'),
]