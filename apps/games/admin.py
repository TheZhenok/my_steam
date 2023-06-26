from django.contrib import admin
from .models import Game, Genre, Company, Comment


admin.site.register(Game)
admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(Comment)
