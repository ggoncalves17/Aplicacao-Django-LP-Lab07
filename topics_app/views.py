from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic
from .forms import TopicForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_topicos(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "topics_app/index.html", context)


#CASO NÃO ESTEJA LOGADO SER REDIRECIONADO PARA A PÁGINA LOGIN

@login_required
def criacao_topicos(request):
    form = TopicForm()
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect("/")
        else:
            form = TopicForm()
    return render(request, "topics_app/criarTopico.html", {"form": form})

@login_required
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)