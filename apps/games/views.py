from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    html_code: str = "<h1>Hello Nibba</h1>"
    response: HttpResponse = HttpResponse(html_code)
    return response

def test_render(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/index.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )
