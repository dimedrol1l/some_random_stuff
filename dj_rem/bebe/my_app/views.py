from random import randint

from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


# Create your views here.


def index(req):
    return HttpResponse('<h1>привет</h1>')


class Products:
    __id = 0

    def __init__(self, name: str,
                 author: str, category: str,
                 price: int) -> None:
        self.id = Products.__id
        self.name = name
        self.author = author
        self.category = category
        self.price = price
        Products.__id += 1

    def __str__(self):
        return f'название {self.name}<br>Автор: {self.author}'


books = [
    Products('bebe', 'bebe', 'bebe', '1500'),
    Products('маленький принц', 'экзеперю', 'сказка', '500'),
    Products('апрол', 'про', 'сказка', '1500'),
    Products('перре', 'роулинг', 'фантастика', '15000')
]


def products_view(req):
    # if 'name' in req.GET:
    #     return HttpResponse(f'привет дорогой, {req.GET["name"]}')
    # if 'name' in req.POST:
    #     return HttpResponse(f'привет дорогой, {req.POST["name"]}')
    if req.POST:
        pr = Products(
            name = req.POST['name'],
            author = req.POST['author'],
            category = req.POST['category'],
            price = req.POST['price'],
        )
        books.append(pr)
    return HttpResponse('<br>'.join([book.name for book in books]))


def product_view(req, prod_num):
    if prod_num >= len(books):
        raise Http404("не найдено")

    return HttpResponse(str(books[prod_num]))