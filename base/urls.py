from django.urls import path,include
from base import urls
from .views import getData
urlpatterns = [
    path('',getData,name="homepage"),
]
