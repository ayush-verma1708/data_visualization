from django.urls import path,include
from base import urls
from . import views
urlpatterns = [
    path('',views.homepage,name="homepage"),
]
