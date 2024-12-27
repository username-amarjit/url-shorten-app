from django.urls import path
from url_app import views

urlpatterns = [
    path('', views.url_shortner_view),
    path('redirect/<str:path>', views.redirect_view),

]
