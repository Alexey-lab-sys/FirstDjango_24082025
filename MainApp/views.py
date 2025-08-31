
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
    html = f"""
    Имя: {USER_DATA['first_name']}<br>
    Отчество: {USER_DATA['middle_name']}<br>
    Фамилия: {USER_DATA['last_name']}<br>
    телефон: {USER_DATA['phone']}<br>
    email: {USER_DATA['email']}<br><br>
    <a href="{reverse('home')}">На главную</a> |
    <a href="{reverse('items_list')}">Список товаров</a>
    """
    return HttpResponse(html)

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
        return HttpResponse("<h2>Товар не найден</h2>")

def items_list(request):
    """Страница со списком товаров"""
    context = {
        'items': items  # Передаем список товаров в шаблон
    }
    return render(request, 'items_list.html', context)
