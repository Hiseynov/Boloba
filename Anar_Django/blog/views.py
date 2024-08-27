from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import *
from .forms import CommentForm
# Create your views here.

def Blog(request):
    context = {
        "text":"Hello my name is Anar"
    }
    return render(request,'blog.html',context=context)

class BlogPost(ListView):
    model = Blogs
    template_name = 'blog.html'
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def BlogDetails(request):
    return render(request,'blog-details.html')

class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(blog=self.object)
        context['form'] = CommentForm()
        context['comments'] = comments
        context['comment_count'] = comments.count()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.save()
            return redirect('blog_details', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


