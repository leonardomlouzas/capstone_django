from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MovieView.as_view()),
    path('movies/<str:movie_uuid>/', views.MovieUuidView.as_view()),
    path('cart/', views.CartListView.as_view()),
    path('cart/pay/', views.PaymentView.as_view()),
    path('cart/pending/', views.CartListPendingView.as_view()),
    path('cart/add/<str:movie_uuid>/', views.CartAddView.as_view()),
    path('cart/<str:cart_uuid>/', views.CartUuidView.as_view()),
]
