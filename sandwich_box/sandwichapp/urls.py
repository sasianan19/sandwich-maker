from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView


urlpatterns = [
    #sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    #sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
]