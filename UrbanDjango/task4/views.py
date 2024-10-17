from django.shortcuts import render


# Create your views here.
def task3_1(request):
    return render(request, 'platform2.html')


def task3_2(request):
    content = {
        'content': ['Пасатижы', 'Отвёртки', 'Шестигранники'],
    }
    return render(request, 'instrument2.html', content)


def task3_3(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart2.html', context)


def menu(request):
    return render(request, 'menu.html')