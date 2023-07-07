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
        self.create_games()
        print("FINISH")
