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

def sendText(request):
    input_text = request.POST['text']

    print(input_text)
    if (not input_text.isdigit()):
        return render(request, 'error.html')

    print(len(database))
    
    num = int(input_text)
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': database[:min(num, len(database))]
    }})

def showTask(request):
    return render(request, 'task.html')