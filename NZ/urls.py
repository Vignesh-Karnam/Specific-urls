from django.urls import path
from NZ.views import *

app_name='NZ'

urlpatterns=[
    path('Williamson/',Williamson,name='Williamson'),
    path('Ravindra/',Ravindra,name='Ravindra'),
]