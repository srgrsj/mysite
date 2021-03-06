from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):
    question = Question.objects.all()
    
    
    context = {
        "questions" : question

    }

    return render(request, "polls/index.html", context)






def meme(request):
    
    return HttpResponse("<img src='https://memepedia.ru/wp-content/uploads/2021/02/povezlo-povezlo-mem-5.jpg'>")


def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }

    return render(request, "polls/detail.html",context)



def results(request, q_id):
    res = "Result for question number %s. " % q_id
    return HttpResponse(res)
def vote(request, q_id):
    res = "Vote for question number %s. " % q_id
    return HttpResponse(res)
