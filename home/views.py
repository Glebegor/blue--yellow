from django.shortcuts import render, redirect
from .forms import formlogin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext
from goods.forms import ordersForm
from django.core.mail import send_mail

def homePage(request):
    data={
        "Title": "Домашня сторінка"
    }
    return render(request, template_name="home/home.html", context=data)
def LoginPage(request):
    formloginView = formlogin()
    if request.method == "POST":
        formloginView = formlogin(request.POST)
        if formloginView.is_valid():
            password = formloginView.cleaned_data["password"]
            username = formloginView.cleaned_data["username"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Ви увійшли в обліковий запис адміністратора')

    data={
        "Title": "Логін сторінка",
        "formlogin": formloginView
    }
    return render(request, template_name="home/login.html", context=data)

def exitPage(request):
    data = {
        "Title": "Вихід"
    }
    logout(request)
    messages.info(request, "Ви вийшли з акаунту") 
    return render(request, template_name="home/exit.html", context=data)

def handler404(request, *args, **argv):
    return render(request,'404.html',RequestContext(request))


def handler500(request, *args, **argv):
        return render(request,'500.html',RequestContext(request))
