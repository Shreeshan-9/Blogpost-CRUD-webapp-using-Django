from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView , DetailView, 
    CreateView, UpdateView, DeleteView
)
from .models import Post

# Create your views here.
# Function based view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # the context is passed into the template
    #  & the keyname 'posts' will be accessible from the template 


# class based view
class PostListView(ListView):
    model = Post  # tells the ListView which model to query in order to create the list 
    template_name = 'blog/home.html' # changing the template name because by default class based views look for 
                                     # template of a certain naming pattern app/model_viewtype.html

    context_object_name = 'posts'  
    ordering = ['-date_posted']  # orders posts from newest to oldest



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # sets the author before running the parent class form_valid() 
        return super().form_valid(form)  # runs the form_valid of the parent class



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title_arg': 'About'})
