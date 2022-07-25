from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MovieView.as_view()),
    path('movies/<str:movie_uuid>/', views.MovieUuidView.as_view()),
]
