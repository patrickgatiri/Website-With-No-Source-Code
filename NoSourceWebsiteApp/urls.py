from django.urls import path
from NoSourceWebsiteApp import views

urlpatterns = [
    path('', views.homepage, name='Home Page'),
    path('style.css', views.cssstylesheet, name="CSS Stylesheet"),
]
