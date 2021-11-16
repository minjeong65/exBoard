from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password


# Create your views here.
def index(request):
    u = User.objects.all()
    context = {
        'u':u
    }
    return render(request, 'acc/index.html', context)


def userlogin(request):
    un = request.POST.get('username')
    pw = request.POST.get('password')
    user = authenticate(username = un, password = pw) #username은 un으로 password는 pw로 받아서 user가 있는지 확인할 수 있음
    
    if user:                
        login(request, user) #로그인 정보가 유효하면
        return redirect('home:index') #로그인 후 홈으로
    else:
        return redirect('acc:signup') #아니면 회원가입



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