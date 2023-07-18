from django.urls import path

# Local
from .views import GameView, about, GameListView, MainView


urlpatterns = [
    path('<int:game_id>/', GameView.as_view()),
    path('list/', GameListView.as_view()),
    path('', MainView.as_view()),
    path('about/', about),
]
