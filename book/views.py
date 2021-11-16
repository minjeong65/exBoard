from django.shortcuts import render,redirect
from .models import Book,Read
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    b=Book.objects.all()
    r=Read.objects.all()
    context={
        'blist' : b,
        'rlist' : r,
    }
    return render(request, 'book/index.html', context)


def create(request):
    if request.method == "POST":
        sn=request.POST.get("sname")
        su=request.POST.get("surl")
        Book(site_name = sn, site_url = su).save()
        return redirect("book:index")
    return render(request, 'book/create.html')


def delete(request, pk):
    b = Book.objects.get(id=pk)
    b.delete()
    return redirect("book:index")


def update(request,pk):
    b = Book.objects.get(pk=pk)

    if request.method == "POST":
        sn = request.POST.get("site_name")
        su = request.POST.get("site_url")
        b.site_name = sn 
        b.site_url = su
        b.save()    
        return redirect('book:index')
    
    context = {
        'b': b 
    }
    return render(request, 'book/update.html', context)


def r_create(request):
    if request.method == "POST": #값은 입력받으면 저장하고 index로 돌아옴
        url = request.POST.get('read_url') #url 받아옴
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select("title")[0].text
        Read(read_url = url, title = title).save()
        return redirect('book:index')
    #아직 값이 입력되지 않았으면 등록 창으로 이동
    return render(request, 'book/r_create.html')


def r_delete(request, pk):
    r = Read.objects.get(pk=pk)
    r.delete()
    return redirect('book:index')