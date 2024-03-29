from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('accounts/', views.AccountView.as_view()),
    path('accounts/<str:user_uuid>/', views.AccountUuidView.as_view()),
]
