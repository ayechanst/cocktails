from django.urls import path
from . import views

urlpatterns = [
    path('cocktails/', views.cocktail_view, name='cocktail view'),
]