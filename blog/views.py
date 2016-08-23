from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    article = Article.objects.all()
    user = request.user if request.user.is_authenticated() else None

    content={
        'user':user,

    }

    return  render(request, 'blog/homepage.html', content)


def article(request):
    article = Article.objects.all()


    content ={
        'article': article,


    }

    return render(request, 'blog/article.html', content)

def contact(request):


    content={}


    return render(request, 'blog/contact.html', content)



def about(request):



    content={}


    return render(request, 'blog/about.html', content)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    content ={
        'article': article,
    }

    return render(request, 'blog/article_detail.html',content)

def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request, 'blog/article_detail.html', pk=article.pk)
    else:
        form = EditForm(instance=article)
    return render(request, 'blog/edit.html', {'form':form})

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == "POST":
        password = request.POST.get('password','')
        repeat_password = request.POST.get('repeat_password','')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username','')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(password=password,username=username,
                                                    email=request.POST.get('email',''))
                # new_user.save()
                state = 'success'
    content = {
        'state':state,
        'user': None,
    }
    return render(request, 'blog/signup.html', content)

def login(request):
    if request.user.is_authenticated():
        return  HttpResponseRedirect(reverse('homepage'))
    state = None

    if request.method == 'POST':
        password = request.POST.get('password','')
        username = request.POST.get('username','')
        user = auth.authenticate(password=password,username=username)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'

    content ={
        'state': state,
        'user': None,
    }
    return render(request, 'blog/login.html', content)

@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password','')
        new_password = request.POST.get('new_password','')
        repeat_password = request.POST.get('repeat_password','')
        if user.check_password(old_password):
            if not new_password:
                state='empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            elif new_password == old_password:
                state = 'password_same'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'blog/set_password.html',content)

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))