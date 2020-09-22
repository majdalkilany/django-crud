from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy, reverse
from . models import Post

class BlogListView(ListView) : 
    template_name = 'posts.html'
    model = Post

class BlogDetailView(DetailView) : 

    template_name = 'post_details.html'
    model  =  Post

class BlogCreateView(CreateView) : 

    template_name = 'post_new.html'
    model  =  Post
    fields = ['title', 'auther', 'body']


class BlogUpdateView(UpdateView) : 

    template_name = 'post_edit.html'
    model  =  Post
    fields = ['title', 'auther', 'body']




class BlogDeleteView(DeleteView) : 

    template_name = 'post_delet.html'
    model  =  Post
    success_url = reverse_lazy('posts')
    
