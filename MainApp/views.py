#from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpResponse, Http404
#from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.

# Данные пользователя
USER_DATA = {
    'first_name': 'Иван',
    'middle_name': 'Петрович',
    'last_name': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}

# Список товаров
items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},
]

def home(request):
    html = f'''
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{USER_DATA["last_name"]} {USER_DATA["first_name"][0]}.{USER_DATA["middle_name"][0]}.</i>
    <br><br>
    <a href="{reverse('about')}">Обо мне</a> |
    <a href="{reverse('items_list')}">Список товаров</a>
    '''
    return HttpResponse(html)

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
    # Ищем товар по ID, если не найден, вызываем 404
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item:
        html = f"""
        <h2>{item['name']}</h2>
        ID товара: {item['id']}<br><br>
        <a href="{reverse('items_list')}">← Назад к списку товаров</a><br>
        <a href="{reverse('home')}">На главную</a> | 
        <a href="{reverse('about')}">Обо мне</a>
        """
    else:
        return HttpResponse("<h2>Товар не найден</h2><br><a href='{reverse('items_list')}'>Назад к списку товаров</a>")
    
    return HttpResponse(html)

def items_list(request):
    """Страница со списком товаров"""
    html = "<h2>Список товаров</h2><ul>"
    for item in items:
        html += f'<li><a href="{reverse("item_detail", args=[item["id"]])}">{item["name"]}</a></li>'
    html += "</ul>"
    html += f'<a href="{reverse("home")}">На главную</a> | '
    html += f'<a href="{reverse("about")}">Обо мне</a>'
    return HttpResponse(html)
