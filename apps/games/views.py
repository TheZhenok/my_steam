from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/index.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )
