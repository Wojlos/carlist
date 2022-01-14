
from django.contrib import admin
from django.urls import path
from api.views import CarGenericApiView, rate_car, get_popular_cars


urlpatterns = [ 
    path('cars/',CarGenericApiView.as_view()),
    path('cars/<int:pk>/',CarGenericApiView.as_view()),
    path('rate/',rate_car),
    path('popular/',get_popular_cars)
]
