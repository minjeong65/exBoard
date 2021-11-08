from django.shortcuts import render,redirect
from .models import Book


# Create your views here.
def index(request):
    b=Book.objects.all()
    context={
        'blist' : b,
    }
    return render(request, 'book/index.html', context)


def detail(request,pk):
    b= Book.objects.get(id=pk)
    context={
        'book' : b,
    }
    return render(request, 'book/detail.html', context)


def create(request):
    if request.method == "POST":
        sn=request.POST.get("sname")
        su=request.POST.get("surl")
        Book(site_name = sn, site_url = su).save()
        return redirect("book:index")
    return render(request, 'book/create.html')

def delete(request, pk):
    b= Book.objects.get(id=pk)
    b.delete()
    return redirect("book:index")

def update(request,pk):
    return redirect("book:index")