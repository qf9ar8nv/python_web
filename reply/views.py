from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from board.models import Post
from reply.forms import ReplyForm
from reply.models import Reply

@login_required(login_url='/user/login')
def create(request, bid):
    if request.method == "POST":
        replyForm = ReplyForm(request.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            reply.writer = request.user
            post = Post()
            post.id = bid
            reply.post = post
            reply.save()

    return redirect('/board/read/'+str(bid))

@login_required(login_url='/user/login')
def like(request, bid):
    reply = Reply.objects.get(id=bid)
    user = request.user
    if reply.like.filter(id=user.id).exists():
        reply.like.remove(user)
        return JsonResponse({'message': 'deleted', 'like_cnt': reply.like.count()})
    else:
        reply.like.add(user)
        return JsonResponse({'message': 'added', 'like_cnt': reply.like.count()})

@login_required(login_url='/user/login')
def delete(request, bid, bid2):
    reply = Reply.objects.get(id=bid)
    if request.user != reply.writer:
        return redirect('/board/read/' + str(bid))
    reply.delete()
    return redirect('/board/read/'+str(bid2))

@login_required(login_url='/user/login')
def update(request, bid, bid2):
    if request.method == 'GET':
        reply = Reply.objects.get(id=bid)
        if request.user != reply.writer:
            return redirect('/board/read/' + str(bid2))
        context = {'reply': reply, 'post_id': bid2}
        return render(request, "reply/update.html", context)
    else:
        reply = Reply.objects.get(id=bid)
        reply.contents = request.POST['contents']
        reply.save()
    return redirect('/board/read/' + str(bid2))
