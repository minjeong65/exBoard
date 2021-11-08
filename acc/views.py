from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password


# Create your views here.
def index(request):
    return render(request, 'acc/index.html')


def userlogin(request):
    un = request.POST.get('username')
    pw = request.POST.get('password')
    user = authenticate(username = un, password = pw) #username은 un으로 password는 pw로 받아서 user가 있는지 확인할 수 있음
    
    if user:                #로그인 정보가 유효하면
        login(request, user) #로그인하고 홈으로 이동
    return redirect('acc:index')



def userlogout(request):
    logout(request)
    return redirect('acc:index')


def signup(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        com = request.POST.get('comment')
        pic = request.FILES.get('pic')
        User.objects.create_user(username = un, password = pw, comment = com, pic=pic)
        return redirect('acc:index')
    return render(request, 'acc/signup.html')


def userinfo(request):
    return render(request, "acc/info.html")


def userdel(request):
    u = User.objects.get(username = request.user.username)
    u.delete()
    return redirect("acc:index")