from django.urls import path

from matrix.views import home

urlpatterns = [
    path('', home, name='home'),

]