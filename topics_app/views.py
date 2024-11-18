from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

def lista_topicos(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "topics_app/index.html", context)

def criacao_topicos(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)