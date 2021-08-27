from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return HttpResponse("<h4>Контакты</h4>")

def news(request):
    return render(request, 'main/news.html')


def prod(request):
    render(request, 'main/prod.html')


def photogallery(request):
    return HttpResponse("<h4>Галерея работ</h4>")