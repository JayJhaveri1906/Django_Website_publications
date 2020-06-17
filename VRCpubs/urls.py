from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path("VRCpubs", views.index,name="index"),
    path("", views.index, name="index"),
    path('<int:year_id>/',views.year_detail, name='year_detail'),
]
