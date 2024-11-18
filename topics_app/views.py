from django.shortcuts import render, redirect, get_object_or_404
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
def detalhes_topicos(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

@login_required
def apagar_topico(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user != topic.author:
        return HttpResponse("Não tem permissão para apagar o evento.", status=403)
    if request.method == "POST":
        topic.delete()
        return redirect("/")
    return render(request, "topics_app/apagarTopico.html", {"topic": topic})


 
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)