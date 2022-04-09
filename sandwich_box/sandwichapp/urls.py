from django.urls import path
from sandwichapp.views import SandwichappView


urlpatterns = [
    #sandwich
    path('', SandwichappView.as_view(), name='sandwich')
]