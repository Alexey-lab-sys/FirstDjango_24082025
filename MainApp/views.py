from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request) -> HttpResponse:
    context = {
        "name": "Требунский Алексей Александрович",
        "email": "a.tredounskiy@gmail.com",
    }
    return render(request, "index.html", context)

def about(request):
    author = {
        'name': 'Алексей',
        'middle_name': 'Александрович',
        'last_name': 'Требунский',
        'phone': '8-916-950-95-29',
        'email': 'a.tredounskiy@gmail.com',
    }
    context = {
        'author': author,
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """ Get item by id from db."""
    try:    
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {'errors': [f'Item with id={item_id} not found']})
    else:
        colors = item.colors.all()
        context = {
            "item": item,
            "colors": colors,
            }
        return render(request, "item_page.html", context)
    

def get_items(request):
    """ Get all items from db."""
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)