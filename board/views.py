from django.shortcuts import render, redirect
from .models import Board


# Create your views here.
def index(request):
    b = Board.objects.all()
    context = {
        'blist' : b,
    }
    return render(request, 'board/index.html', context)


def detail(request,pk):
    b = Board.objects.get(pk=pk)
    context = {
        'b':b
    }
    return render(request, 'board/detail.html', context)


def create(request):
    if request.method == "POST":
        sb=request.POST.get("subject")
        wr= request.user.username
        cn=request.POST.get("content")
        p = request.FILES.get("photo")
        Board(subject = sb, writer = wr, content = cn, photo = p).save()
        return redirect("board:index")
    return render(request, 'board/create.html')


def delete(request,pk):
    b = Board.objects.get(id=pk)
    b.delete()
    return redirect('board:index')


def update(request, pk):
    b = Board.objects.get(id=pk)
    
    if request.method == "POST":
        sb = request.POST.get("subject")
        wr= request.user.username
        cn=request.POST.get("content")
        p=request.FILES.get("photo")
        b.subject = sb
        b.writer = wr
        b.content = cn
        b.photo = p
        b.save()
        return redirect('board:detail', pk=pk)
    context = {
        'b':b
    }
    return render(request, 'board/update.html', context)
