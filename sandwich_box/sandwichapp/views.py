from django.shortcuts import render
from django.views import View

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