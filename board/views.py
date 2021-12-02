from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    #페이징할 때
    page = request.GET.get('page',1) #page값 없이 호출된 경우에는 디폴트로 1을 설정
    cate = request.GET.get('cate','')
    kw = request.GET.get('kw','')

    # 조회할 때
    if kw:
        if cate == "subject":
            b = Board.objects.filter(subject__startswith=kw).order_by("-ctime")
        elif cate == "writer":
            b = Board.objects.filter(writer=kw).order_by("-ctime")
        else:
            b = Board.objects.filter(content__contains=kw).order_by("-ctime")
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


def detail(request, pk):
    if not request.user.username:
        return redirect("acc:index")
    b = Board.objects.get(id=pk)
    r = b.reply_set.all()
    context = {
        'b' : b,
        'rep' : r,
    }
    return render(request, "board/detail.html", context)

def create(request):
    if request.method == "POST":
        sb = request.POST.get("subject")
        wr = request.user.username
        cn = request.POST.get("content")
        p = request.FILES.get("photo")
        ct = timezone.now()
        Board(subject = sb, writer = wr, content = cn, photo = p, ctime = ct).save()
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


def reply(request, pk):
    b = get_object_or_404(Board,pk=pk)
    if request.method == "POST":
        rep = request.user.username
        com = request.POST.get("comment")
        ct = timezone.now()
        Reply(sub = b, replyer = rep, comment = com, create_time = ct).save()
    return redirect('board:detail', pk=pk)


def del_rep(request, num):
    re = get_object_or_404(Reply,pk=num)
    re.delete()
    return redirect('board:detail', pk = re.sub.id)


def mod_rep(request, num):
    return render('board:detail', pk=num)