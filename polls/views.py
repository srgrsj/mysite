from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


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
        "question" : question,
    }

    return render(request, "polls/detail.html",context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)

    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()


    
    return HttpResponseRedirect( reverse("polls:results", args=(q_id, )) )


def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question,
    }

    return render(request, "polls/results.html",context)


