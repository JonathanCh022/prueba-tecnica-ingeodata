from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.postApp.form import UserForm, PostForm, CommentForm
from apps.postApp.models import User, Post, Comment
from django.views import View

# Create your views here.


class MyFormAddShowView(View):
    """Clase del tipo View que recibe las peticiones de tipo GET que devuelve el formulario para crear un usuario y de
      tipo POST que recibe la informacion del formulario diligenciado y los guarda"""

    form_class = UserForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        users = User.objects.all()
        return render(request, "form_template.html", {'form': form, 'users': users})

    def get(self, request):
        form = self.form_class()
        users = User.objects.all()
        return render(request, "form_template.html", {'form': form, 'users': users})


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
    return render(request, 'update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


class MyFormAddPost(View):
    form_class = PostForm

    def post(self, request):
        form_post = self.form_class(request.POST)
        if form_post.is_valid():
            form_post.save()
        posts = Post.objects.all()
        return render(request, "post_template.html", {'form': form_post, 'posts': posts})

    def get(self, request):
        form_post = self.form_class()
        posts = Post.objects.all()
        return render(request, "post_template.html", {'form': form_post, 'posts': posts})


def update_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        fm = PostForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Post.objects.get(pk=id)
        fm = PostForm(instance=pi)
    return render(request, 'post_update.html', {'form': fm})


def delete_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/posts')


class FormAddComment(View):
    form_class = CommentForm

    def post(self, request):
        form_comment = self.form_class(request.POST)
        if form_comment.is_valid():
            form_comment.save()
        comments = Comment.objects.all()
        return render(request, "comment_template.html", {'form': form_comment, 'comments': comments})

    def get(self, request):
        form_comment = self.form_class()
        comments = Comment.objects.all()
        return render(request, "comment_template.html", {'form': form_comment, 'comments': comments})


def update_comment(request, id):
    if request.method == 'POST':
        pi = Comment.objects.get(pk=id)
        fm = CommentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Comment.objects.get(pk=id)
        fm = CommentForm(instance=pi)
    return render(request, 'comment_update.html', {'form': fm})


def delete_comment(request, id):
    if request.method == 'POST':
        pi = Comment.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/comment')
