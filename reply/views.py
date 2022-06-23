from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from board.models import Post
from reply.forms import ReplyForm

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