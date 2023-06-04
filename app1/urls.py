from django.urls import path
from app1.views import*
app_name='images2'
urlpatterns=[
    path('shiva/',shiva,name='shiva')
]