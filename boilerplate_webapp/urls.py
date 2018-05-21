"""
URL routing schema for Boilerplate Webapp.

"""

from django.urls import path

from . import views

app_name = "boilerplate_webapp"

urlpatterns = [
    path('example', views.example, name='example'),
]
