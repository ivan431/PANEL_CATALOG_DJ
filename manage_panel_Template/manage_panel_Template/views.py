from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная стр.":"/", "каталог":"/catalog", "о приложении":"/about"}

def main_page(request):
    title = "Главная страницп приложения"
    data={"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)

#def catalog_page(request):
#    title = "Каталог"
#    data = {"menu": MENU, "title": title}
#    return render(request, "./catalog.html", context=data)

def about(request):
    title = "О чем приложение"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)
