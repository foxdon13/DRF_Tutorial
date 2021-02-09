from django.urls import path
from .views import employeeView

urlpatterns = [
    path('firstApp/',employeeView,name = 'home'),
]