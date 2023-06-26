from django.urls import path

# Local
from .views import index, about


urlpatterns = [
    path('/', index),
    path('about/', about)
]
