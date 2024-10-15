from django.shortcuts import render


# Create your views here.
def task3_1(request):
    title = 'Главная'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def task3_2(request):
    title = 'Инструменты'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'instrument.html', context)


def task3_3(request):
    title = 'Корзина'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
