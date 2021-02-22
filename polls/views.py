from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def meme(request):
    return HttpResponse("<img src='https://memepedia.ru/wp-content/uploads/2021/02/povezlo-povezlo-mem-5.jpg'>")