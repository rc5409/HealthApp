from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_view, name='home'),
    # path('together-ai/', views.together_ai_view, name='together_ai'),
    path('together-ai/', views.together_ai_view, name='together_ai'),
]
