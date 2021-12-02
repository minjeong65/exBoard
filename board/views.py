from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count


# Create your views here.
def index(request):
    #페이징할 때
    page = request.GET.get('page',1) #page값 없이 호출된 경우에는 디폴트로 1을 설정
    cate = request.GET.get('cate','')
    kw = request.GET.get('kw','')

    # 정렬
    if cate == "추천순":
        print(1)
        b = Board.objects.annotate(num_voter = Count('voter')).order_by("-num_voter","-ctime")
    elif cate == "댓글순":
        print(2)
        b = Board.objects.annotate(num_rep = Count('sub')).order_by("-num_rep","-ctime")
    else:
        print(3)
        b = Board.objects.order_by("-ctime")


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
    b = Board.objects.get(pk=pk)
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


# def mod_rep(request, num):
#     re = Reply.objects.get(pk=num)
#     if request.method == "POST":
#         sb = request.POST.get("sub")
#         rep = request.user.username
#         cn = request.POST.get("comment")
#         ct = timezone.now()
#         re.sub = sb
#         re.replyer = rep
#         re.comment = cn
#         re.create_time = ct
#         re.save()
#         return redirect('board:index')

#     context = {
#         'rep': re
#     }
#     return render(request, 'board/mod_rep.html', context)

def voter(request, pk):
    b = get_object_or_404(Board,pk=pk)
    # 추천은 한번만 누를 수 있도록
    if request.user in b.voter.all():
        return redirect('board:detail', pk=pk)
    b.voter.add(request.user)
    return redirect('board:detail', pk=pk)
