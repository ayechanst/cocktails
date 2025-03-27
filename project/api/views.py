from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import get_all_ingredients, get_cocktail_by_letter, get_cocktail_by_name

def home(request):
    return HttpResponse("Welcome to the Home Page")

def cocktail_page(request):
    return render(request, 'template.html')

# request is a HttpsRequest object
def cocktail_view(request):
    cocktail_name = request.GET.get('name', 'margarita') # .get(key, default value) from 
    data = get_cocktail_by_name(cocktail_name)
    return JsonResponse(data, safe=False)

def cocktail_letter_view(request):
    cocktail_letter = request.GET.get('letter','a')
    data = get_cocktail_by_letter(cocktail_letter)
    return JsonResponse(data, safe=False)

def cocktail_ingredients(request):
    data = get_all_ingredients()
    return JsonResponse(data, safe=False)


