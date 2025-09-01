from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

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
    # Ищем товар по ID
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item:
        # Передаем данные о товаре в шаблон
        context = {
            'name': item['name'],
            'quantity': item['quantity'],
        }
        return render(request, 'item.html', context)
    else:
        # Если товар не найден, возвращаем 404
        return render(request, '404.html', status=404)


def items_list(request):
    """Страница со списком товаров"""
    context = {
        'items': items  # Передаем список товаров в шаблон
    }
    return render(request, 'items_list.html', context)