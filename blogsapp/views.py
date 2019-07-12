from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Blog, Comment
from django.views.generic import ListView
from . forms import CommentForm



class blogview(ListView):
    model = Blog
    template_name= 'view_blog.html'
    context_object_name = "viewblog"


def Detail_view(request,pk):
    c_form = CommentForm()
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog, reply=None)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            comment = request.POST.get('comment')
            Name = request.POST.get('Name')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(pk=reply_id)
            comment= Comment.objects.create(blog=blog, Name=Name, comment=comment, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(blog.get_absolute_url())
        else:
            c_form = CommentForm()
    context = {
       'blog':blog,
       'comments':comments,
       'c_form':c_form,
    }
    return render(request,'single.html',context)
