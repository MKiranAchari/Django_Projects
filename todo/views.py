from django . shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todoo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.POST.get('submit'):
        return redirect('/loginn')

    if request.method == 'POST':
        un = request.POST.get('username')
        email = request.POST.get('email')
        pws = request.POST.get('password')
        print(un,email,pws)
        new_user = User.objects.create_user(un,email,pws)
        new_user.save()
        return redirect('/loginn')
    
    return render(request,'signup.html')

def loginn(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pws = request.POST.get('password')
        print(un,pws)
        user = authenticate(request,username=un,password=pws)
        if user is not None:
            login(request,user)
            return redirect('/todo')
        return redirect('/loginn')
        
    return render(request,"loginn.html")

@login_required(login_url='loginn/')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Todoo(title=title, user = request.user)
        obj.save()
        res = models.Todoo.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo',{'res':res})
    
    res = models.Todoo.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res':res})

@login_required(login_url='loginn/')
def update(request,sno):
    if request.method == 'POST':
        title = request.POST.get('updateTask')
        print(title)
        obj = models.Todoo.objects.get(sno=sno)
        obj.title=title
        obj.save()
        user=request.user
        return redirect('/todo',{'obj':obj})
    
    obj = models.Todoo.objects.get(sno=sno)
    res = models.Todoo.objects.filter(user=request.user).order_by('-date')
    return render(request,'update.html',{'res':res,'obj':obj})

@login_required(login_url='loginn/')
def delete(request,sno):
    obj = models.Todoo.objects.get(sno=sno)
    obj.delete()
    return redirect('/todo')

def signout(request):
    logout(request)
    return redirect('/loginn')