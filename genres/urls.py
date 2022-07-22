from django.urls import path


from genres.views import GenreView, GenreSingleView

urlpatterns = [
    path("genres/", GenreView.as_view()),
    path("genres/<str:genre>/", GenreSingleView.as_view()),
]
