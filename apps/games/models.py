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

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

    def __str__(self) -> str:
        return self.name    


class Genre(models.Model):
    """Game genre."""

    name = models.CharField(
        verbose_name='название',
        max_length=130,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return self.name


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
        to=Company,
        on_delete=models.CASCADE,
        related_name='company_games'
    )
    genres = models.ManyToManyField(
        verbose_name='жанры',
        to=Genre,
        related_name='games'
    )

    class Meta:
        ordering = ('price', 'name')
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __str__(self) -> str:
        return f'{self.company} | {self.name} | {self.price}$'


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

    class Meta:
        ordering = ('-id',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self) -> str:
        rate_str = '★' * self.rate 
        return f'{self.user.username} оценка:   {rate_str}'