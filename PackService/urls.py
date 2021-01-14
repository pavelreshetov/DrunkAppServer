from django.urls import path, include
from .views.example import Test

urlpatterns = [
    path('', Test().test, name='test')
]
