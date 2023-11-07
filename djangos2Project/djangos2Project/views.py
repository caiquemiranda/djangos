from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello mundo!')

def articles(request, year):
    return HttpResponse(f'O ano do artigo é {str(year)}')