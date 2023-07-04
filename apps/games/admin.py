from django.contrib import admin

from typing import Union , TypeAlias
# Register your models here.

from .models import Game, Genre, Company, Comment , WishList , Order , InviteCard

MyType: TypeAlias = tuple[tuple[Union[str ,dict[str,list[str]]]]]

class GameAdmin(admin.ModelAdmin):

    list_display:list[str] = (
        'name',
        'company',
        'datetime_created'    
    )

    list_filter: list[str] = (
        'company',
    )
    fieldsets:MyType = (
        (
            'Public for my game shop!',
            {
                'classes':['wide','extrapretty'],
                'fields':[
                    'name',
                    'price',
                    'genres'
                ]
            }
        ),
        (
            'Private information',
            {
                'classes':['collapse'],
                'fields':[
                    'datetime_created',
                    'company'
                ]
            }
        ),
        
    )
    readonly_fields:list[str] = [
        'datetime_created'
    ]

    def get_readonly_fields(
        self, request , obj =...)-> list[str]:
        if obj is not None:
            return self.readonly_fields
        return []

class CompanyAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'name',
        'datetime_created',
    )
     list_filter: list[str] = (
        'datetime_created',
    )

class GenresAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'name',
    )


class CommentsAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'user',
        'game',
        'text'
    )
     list_filter: list[str] = (
        'game',
    )
     
class WhishListAdmin(admin.ModelAdmin):

    list_filter: list[str] = (
        'games',
    )

class OrderAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'user',
        'game',
        'method'
    )
    list_filter: list[str] = (
        'game',
    )

class InviteCardAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'owner',
        'counter'
    )
    list_filter: list[str] = (
        'owner',
    )   

admin.site.register(Game , GameAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Genre , GenresAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(WishList, WhishListAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(InviteCard, InviteCardAdmin)

