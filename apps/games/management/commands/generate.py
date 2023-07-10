import requests
import random
import datetime
from typing import Any, Optional
from django.core.management import BaseCommand
from django.db.models.query import QuerySet
from django.db.utils import IntegrityError

from games.models import (
    Genre,
    Game,
    Company
)


class Command(BaseCommand):
    """Command for generate data for Database."""

    def create_companies(self) -> None:
        _companies_name_pattern: set[str] = {
            'Xbox Game Studios',
            'MrSuicideSheep',
            'Ubisoft',
            'Electronic Arts',
            'Hitman',
            'CarX Technologies',
            'SEGA',
            'FF Digital',
            'Bethesda',
            '2K',
            'Valve',
            'Half-Life',
            'Telltale Games',
            'KONAMI',
            'Age of Empires Franchise',
            'Yogscast Games',
            'Keplerians',
            'Gameloft',
            'Ironhide Game Studio',
            'Innersloth',
            'Digital Extremes Ltd.',
            'Bandai Namco Entertainment',
            'Monolith Productions',
            'Capcom',
            'Studio Wildcard',
            'CM Games VR',
            'Two Star Games',
            'Techland Publishing',
            'Square Enix',
            'Total War Official',
            'CodeParade',
            'Berzerk Studio',
            'HandyGames',
            'ATLUS',
            'PlayStation Studios™',
            '11 bit studios',
            'SCS Software',
            'Monster Hunter',
            'CD PROJEKT RED',
            'GrabTheGames Publishing',
            'Paradox Interactive - Official',
            'tinyBuild',
            'Sniper Ghost Warrior Franchise',
            'Stunlock Studios',
            'Wargaming Group Ltd.',
            'KOEI TECMO',
            'Rockstar Games',
            'Assassins Creed',
            'Obsidian Entertainment',
            'Starbreeze Home',
            'CrytekOfficial',
            '98DEMAKE',
            'Ankama',
            'MoeNovel',
            'Fatshark',
            'PlayWay S.A.',
            'WB Games',
            'Flow Studio',
            'Landfall Games',
            'SMG Studio',
            'Steel Wool Studios',
        }
        
        name: str
        for name in _companies_name_pattern:
            day: int = random.randint(1, 25)
            month: int = random.randint(1, 12)
            year: int = random.randint(1995, 2023)
            minute: int = random.randint(1, 59)
            hour: int = random.randint(1, 23)
            try:
                Company.objects.create(
                    name=name,
                    datetime_created=datetime.datetime(
                        year=year,
                        month=month,
                        day=day,
                        minute=minute,
                        hour=hour
                    )
                )
            except IntegrityError:
                print(f'Company {name} already exists!')

    def create_genres(self) -> None:
        _genres_pattern: set[str] = {
            'Одиночная игра',
            'Мультиплеер',
            'Для одиноких',
            'Кросс-платформенный',
            'Головоломка',
            'Сногшибательная',
            'Скучная',
            'Весёлая',
            'Открытый мир',
            'Закрытый мир',
            'ЛЕГЕНДАРНАЯ',
            'Для олдов',
            'Куда это ты?',
            'А это что такое?',
            'Симулятор'   
        }
        gn: str
        for gn in _genres_pattern:
            try:
                Genre.objects.create(name=gn)
            except IntegrityError as e:
                print(f'Жанр {gn} уже существует')

    def create_games(self) -> None:
        headers: dict[str, str] = {
            "X-RapidAPI-Key": "44bfa356a1mshc9b913b6479a122p1a88fcjsn7c87ef2d0d5c",
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }
        querystring: dict[str, str] = {
            "lowerPrice":"0",
            "steamRating":"0",
            "desc":"0",
            "output":"json",
            "steamworks":"0",
            "sortBy":"Deal Rating",
            "AAA":"0",
            "pageSize":"500",
            "exact":"0",
            "upperPrice":"50",
            "pageNumber":"0",
            "onSale":"0",
            "metacritic":"0",
            "storeID[0]":"1,2,3"
        }
        url = "https://cheapshark-game-deals.p.rapidapi.com/deals"
        response: requests.Response = \
            requests.get(url, headers=headers, params=querystring)
        
        response_games: list[dict[str, str]] = response.json()

        companies: QuerySet[Company] = Company.objects.all()
        genres: QuerySet[Genre] = Genre.objects.all()

        game: dict[str, str]
        for game in response_games:
            try:
                temp_game: Game = Game.objects.create(
                    name=game['title'],
                    price=game['normalPrice'],
                    datetime_created=datetime.datetime.fromtimestamp(
                        game['releaseDate']
                    ),
                    company=random.choice(companies)
                )
                for _ in range(random.randint(0, 10)):
                    temp_game.genres.add(
                        random.choice(genres)
                    )

                temp_game.save()
            except IntegrityError as e:
                print("Game {} already exists".format(
                    game['title']
                ))


    def handle(self, *args, **kwargs):
        self.create_genres()
        self.create_companies()
        self.create_games()
        print("FINISH")
