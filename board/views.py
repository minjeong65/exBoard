from django.shortcuts import render, redirect
from .models import Board
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #페이징할 때
    page = request.GET.get('page',1)
    cate = request.GET.get('cate','')
    kw = request.GET.get('kw','')

    # 조회할 때
    if kw:
        if cate == "subject":
            b = Board.objects.filter(subject__icontains = kw)
        elif cate == 'writer':
            b = Board.objects.filter(writer=kw)
        elif cate == "content":
            b = Board.objects.filter(content__icontains = kw)
    else:
        b = Board.objects.all()
    b = b.order_by('-ctime')
    pag = Paginator(b,10)
    obj = pag.get_page(page)

    context = {
        'blist' : obj,
        'cate' : cate,
        'kw' : kw
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
        sb = request.POST.get("subject")
        wr = request.user.username
        cn = request.POST.get("content")
        p = request.FILES.get("photo")
        Board(subject = sb, writer = wr, content = cn, photo = p, ctime = timezone.now()).save()
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
