from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# from project.api.utils import get_cocktail_by_name
from .utils import get_cocktail_by_name

# Create your views here.

def cocktail_view(request):
    cocktail_name = request.GET.get('name', 'margarita')
    data = get_cocktail_by_name(cocktail_name)
    return JsonResponse(data, safe=False)

def home(request):
    return HttpResponse("Welcome to the Home Page")

