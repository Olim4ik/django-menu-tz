from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


def index(request, pk=None):
    # if request.method == "GET":
    #     query = Menu.objects.filter(url=request.path)
    #     if not query:
    #         print('CHECK')

    menu = Menu.objects.all()

    context = {'menu': menu}
    return render(request, 'menu/index.html', context)
