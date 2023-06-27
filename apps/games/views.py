# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet

# Local
from .models import Game


def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/index.html'
    qs: QuerySet[Game] = Game.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={
            'games': qs
        }
    )

def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

def get_game(request: HttpRequest, game_id: int) -> HttpResponse:
    try:
        game: Game = Game.objects.get(id=game_id)
    except Game.DoesNotExist as e:
        return HttpResponse(
            f'<h1>Игры с id {game_id} не существует!</h1>'
        )
    return HttpResponse(
        f'<h1>ID: {game.name}</h1>'
    )
