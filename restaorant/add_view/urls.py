from django.urls import path
from . import views

urlpatterns = [
    path('rest/', views.home, name='home_rest'),
    path('rest/add', views.add_rest, name='add_rest'),
    path('rest/details/<int:id>', views.details, name='details'),
]