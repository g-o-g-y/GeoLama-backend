from django.urls import path
from . import views

from django.urls import path

from .views import getCoordsAPIView, setCoordsAPIView

app_name = 'game'
urlpatterns = [
    path('pano/', getCoordsAPIView.as_view()),
    path('coords/', setCoordsAPIView.as_view()),
]