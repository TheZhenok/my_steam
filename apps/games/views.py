# Python
import uuid

# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.db.models.functions import Lower
from django.views.generic import View
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import Game, Genre, Company


class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/index.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    

class GameListView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/video.html'
        queryset: QuerySet[Game] = Game.objects.all().order_by('-id')
        genres: QuerySet[Genre] = Genre.objects.all()
        return render(
            request=request,
            template_name=template_name,
            context={
                'games': queryset,
                'genres': genres
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data: dict = request.POST
        files: dict = request.FILES

        image: InMemoryUploadedFile = None
        if files != {}:
            image = files.get('main_imgor')
            image.name = f'{uuid.uuid1()}.png'

        try:
            company: Company = Company.objects.annotate(
                lower_igor=Lower('name')
            ).get(
                lower_igor=str(data.get('company')).lower()
            )
        except Company.DoesNotExist:
            return HttpResponse(
                f"Компании {data.get('company')} не существует"
            )
        
        game: Game = Game.objects.create(
            name=data.get('name'),
            price=float(data.get('price')),
            datetime_created=data.get('datetime_created'),
            company=company,
            main_imgor=image
        )

        key: str
        for key in data:
            if 'genre_' in key:
                genre: Genre = Genre.objects.get(
                    id=int(key.strip('genre_'))
                )
                game.genres.add(genre)

        game.save()
        return HttpResponse("Hello")

class GameView(View):

    def get(self, request: HttpRequest, game_id: int) -> HttpResponse:
        try:
            game: Game = Game.objects.get(id=game_id)
        except Game.DoesNotExist as e:
            return HttpResponse(
                f'<h1>Игры с id {game_id} не существует!</h1>'
            )
        return render(
            request=request,
            template_name='games/store-product.html',
            context={
                'igor': game 
            }
        )
    
def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

