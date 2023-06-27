from django.urls import path

# Local
from .views import index, about, get_game


urlpatterns = [
    path('', index),
    path('about/', about),
    path('<int:game_id>/', get_game)
]
