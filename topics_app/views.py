from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def lista_topicos(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "topics_app/index.html", context)


@login_required
def criacao_topicos(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect("/")
    
    else:
        form = TopicForm()
    return render(request, "topics_app/criarTopico.html", {"form": form, "title": "Criar Novo Tópico"})


@login_required
def detalhes_topicos(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, "topics_app/detalhesTopico.html", {"topic": topic})


@login_required
def apagar_topico(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user != topic.author:
        return render(request, "topics_app/semPermissao.html", {"text": "Não tem permissão para apagar o tópico."}, status=403)
    if request.method == "POST":
        topic.delete()
        return redirect("/")
    return render(request, "topics_app/apagarTopico.html", {"topic": topic, "title": "Apagar Tópico"})


@login_required
def editar_topico(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user != topic.author:
        return render(request, "topics_app/semPermissao.html", {"text": "Não tem permissão para editar o tópico."}, status=403)
    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect("/")
    else:
        form = TopicForm(instance=topic)
    return render(request, "topics_app/criarTopico.html", {"form": form, "title": "Editar Tópico"})

@login_required
def criacao_comentarios(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect('topic_detail', topic_id)
    else:
        form = CommentForm()
    return render(request, "topics_app/criarComentario.html", {"form": form, "title": "Criar Comentário"})

@login_required
def editar_comentario(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return render(request, "topics_app/semPermissao.html", {"text": "Não tem permissão para editar o comentário."}, status=403)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('topic_detail', comment.topic.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "topics_app/criarComentario.html", {"form": form, "title": "Editar Comentário"})

@login_required
def apagar_comentario(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return render(request, "topics_app/semPermissao.html", {"text": "Não tem permissão para apagar o comentário."}, status=403)
    if request.method == "POST":
        comment.delete()
        return redirect('topic_detail', comment.topic.id)
    return render(request, "topics_app/apagarTopico.html", {"comment": comment, "title": "Apagar Comentário"})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/admin")





