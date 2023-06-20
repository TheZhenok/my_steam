from django.urls import path

# Local
from .views import index, test_render


urlpatterns = [
    path('main/', index),
    path('render/', test_render)
]
