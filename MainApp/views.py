from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.

USER_DATA = {
    'first_name': 'Иван',
    'middle_name': 'Петрович',
    'last_name': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
    }


items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},
]



def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И. П.</i>
    """

    return HttpResponse(text)



def about(request):
    return HttpResponse(f"""
    Имя: {USER_DATA['first_name']}<br>
    Отчество: {USER_DATA['middle_name']}<br>
    Фамилия: {USER_DATA['last_name']}<br>
    телефон: {USER_DATA['phone']}<br>
    email: {USER_DATA['email']}<br><br>
    <a href="/">На главную</a>
    """)
 




def item_detail(request, item_id):
    # Находим товар по id
    item = next((item for item in items if item["id"] == item_id), None)
    
    if item is not None:
        return HttpResponse(item["name"])
    else:
        return HttpResponse("Товар не найден", status=404)

