from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello mundo!')

def articles(request, year):
    return HttpResponse(f'O ano do artigo é {str(year)}')

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Maria', 'idade': 18},
        {'nome': 'Pedro', 'idade': 40},
        {'nome': 'Marcos', 'idade': 32},
        {'nome': 'João', 'idade': 23}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa

    return {'nome': 'Não encontrado!', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse(str(result['nome']) + " foi encontrado(a)!, ela tem " + str(result['idade']) + " anos.")
    else:
        return HttpResponse("Pessoa não encontrada!")
