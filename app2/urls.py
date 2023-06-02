from django.urls import path
from app2.views import *
app_name='bbb'

urlpatterns=[
    path('bye/',bye,name='bye'),
]