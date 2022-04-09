from django.shortcuts import render
from django.views import View

ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}

# Create your views here.
class SandwichappView(View):
    def get(self, request):
        if request.method == 'GET':
            return render(
                request = request, 
                template_name ='home.html', 
                context = {'ingredients': ingredients.keys()}
                )

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context = {'ingredients': ingredients[ingredient_type], 'ingredient_type': ingredient_type}
        )