from django.urls import path,include
from base import urls
from .views import getData , homepage , get_data_api , dashboard_view
urlpatterns = [
    path('',getData,name="index"),
    path('homepage/',homepage , name ="homepage"),
    path('api/get-data/', get_data_api, name='get_data_api'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
]
