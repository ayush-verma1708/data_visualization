from django.urls import path,include
from base import urls
from .views import getData , homepage , get_data_api , dashboard_view , filter_Data , deleteAllData

urlpatterns = [
    path('',getData,name="index"),
    path('homepage/',homepage , name ="homepage"),
    path('api/get-data/', get_data_api, name='get_data_api'),
    path('api/loadData', getData, name='get_data'),
    path('dashboard/', dashboard_view, name='dashboard'), 
    path('filter_data/', filter_Data, name='filter_data'), 
    path('delete_data/', deleteAllData, name='delete_data'), 
]