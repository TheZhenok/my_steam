from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    """Game company."""

    name = models.CharField(
        verbose_name='имя',
        max_length=250,
        unique=True
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания'
    )


class Genre(models.Model):
    """Game genre."""

    name = models.CharField(
        verbose_name='название',
        max_length=130,
        unique=True
    )


class Game(models.Model):
    """Game from steam."""

    name = models.CharField(
        verbose_name='имя',
        max_length=250,
        unique=True
    )
    price = models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=12
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания'
    )
    company = models.ForeignKey(
        verbose_name='компания',
        to=Comment,
        on_delete=models.CASCADE,
        related_name='company_games'
    )
    genres = models.ManyToManyField(
        verbose_name='жанры',
        to=Genre,
        related_name='games'
    )


class Comment(models.Model):
    """Comment for games and comp."""
    
    user = models.ForeignKey(
        verbose_name='кто оставил',
        to=User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='текст',
        max_length=254
    )
    rate = models.IntegerField(
        verbose_name='рейтинг',
    )
    game = models.ForeignKey(
        verbose_name='игра',
        related_name='game_comments',
        to=Game,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        verbose_name='компания',
        related_name='company_comments',
        to=Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
