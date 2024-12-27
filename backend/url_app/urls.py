from django.urls import path
from url_app import views

urlpatterns = [
    path('/', views.urlShortnerView),
]
