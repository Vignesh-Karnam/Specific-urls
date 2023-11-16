from django.urls import path
from India.views import *

app_name='India'

urlpatterns=[
    path('Virat/',Virat,name='Virat'),
    path('Shreyas',Shreyas,name='Shreyas'),
]