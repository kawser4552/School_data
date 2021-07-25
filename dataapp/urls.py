from django.urls import path
from .views import *

app_name = 'dataapp'

urlpatterns = [
    path('',index, name='index'),
    path('form/',form, name='form'),
    path('details/<int:id>',details, name='details'),
    path('update/<int:id>',update, name='update'),
    path('delete/<int:id>',delete, name='delete'),
   

]
