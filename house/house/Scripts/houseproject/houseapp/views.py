from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Property,Shortlist
from django.contrib.auth.models import User
from django.views.generic import DeleteView

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'adduser.html',context)

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')

def homelist(request):
    # hl=Property.objects.all()
    # context={'hl':hl}
    # return render(request,'property.html',context)
    # uid=request.session.get('uid')
    hl=Property.objects.filter()
    inc=set()
    for i in hl:
        inc.add(i.city)
    context={'hl':hl,'inc':inc}
    return render(request,'property.html',context)

def add_to_cart(request,pid):
    product_id=Property.objects.get(id=pid)
    uid=request.session.get('uid')
    user_id=User.objects.get(id=uid)
    c=Shortlist()
    c.product=product_id
    c.user=user_id
    c.save()
    return redirect('/hlist')

def cartlist(request):
    uid=request.session.get('uid')
    # user_id=User.objects.get(id=uid)
    cl=Shortlist.objects.filter(user=uid)
    context={'cl':cl}
    return render(request,'cartlist.html',context)

def search(request):
    # uid=request.session.get('uid')
    srch=request.POST.get('srch')
    hl=Property.objects.filter(owner_name__contains=srch)
    context={'hl':hl}
    return render(request,'property.html',context)

class delete(DeleteView):
    template_name='delete.html'
    model=Shortlist
    success_url= '/cartlist'

def sortby_type(request,ixt2):
    # uid=request.session.get('uid')
    hl=Property.objects.filter()
    inc=set()
    for i in hl:
        inc.add(i.city)
        hl=Property.objects.filter(city=ixt2)
    context={'hl':hl,'inc':inc}
    return render(request,'property.html',context)
