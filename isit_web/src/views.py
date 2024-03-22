from django.shortcuts import render
from datetime import date
from src.database.database_tmp import database

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': database
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'order': database[id - 1],
    }})

def defFilter(request):
    input_text = 'а'

    filterData = [];
    for data in database:
        if input_text.lower() in data.get('title').lower():
            filterData.append(data)

    return render(request, 'orders.html', {'data' : {
        'input': input_text,
        'data': filterData
    }})

def filter(request):
    input_text = request.POST['text']
    if input_text == "":
        input_text = 'а'

    filterData = [];
    for data in database:
        if input_text.lower() in data.get('title').lower():
            filterData.append(data)

    return render(request, 'orders.html', {'data' : {
        'input': input_text,
        'data': filterData
    }})

def index(request):
    items_per_page = 10
    total_items = 50
    total_pages = -(-total_items // items_per_page)  # округление вверх

    return render(request, 'pagination.html', {
        'total_pages': total_pages,
        'data' : database
        })


def showTask(request):
    return render(request, 'task.html')