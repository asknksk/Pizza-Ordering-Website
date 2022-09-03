from .views import home, order
from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('order/', order, name="order"),
]
