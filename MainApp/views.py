from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Item

# Create your views here.

# Данные пользователя
USER_DATA = {
    'first_name': 'Алексей',
    'middle_name': 'Александрович',
    'last_name': 'Требунский',
    'phone': '8-916-950-95-29',
    'email': 'a.tredounskiy@gmail.com'
}

# Список товаров
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]

def home(request) -> HttpResponse:
    context = {
        "name": "Требунский Алексей Александрович",
        "email": "a.tredounskiy@gmail.com"
    }
    return render(request, "index.html", context)

def about(request):
    context = USER_DATA  # Передаем данные пользователя в шаблон
    return render(request, "about.html", context)


def item_detail(request, item_id):
    """Страница товара по ID"""
    # Извлекаем товар из базы данных по ID
    item = get_object_or_404(Item, id=item_id)
    
    # Передаем данные о товаре в шаблон
    context = {
        'name': item.name,
        'brand': item.brand,
        'count': item.count,
    }
    return render(request, 'item.html', context)


def items_list(request):
    """Страница со списком товаров"""
    items = Item.objects.all()  # Извлекаем все товары из базы данных
    context = {
        'items': items  # Передаем список товаров в шаблон
    }
    return render(request, 'items_list.html', context)