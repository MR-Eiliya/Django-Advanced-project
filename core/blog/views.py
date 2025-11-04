from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin




# Function base vieww
'''def indexView(request):
    """
    a function base view to show the index page
    """
    name = "Iliya"
    context = {"name":name}
    return render(request,"index.html",context)
'''

class IndexView(TemplateView):
    """
    a class base view to show the index page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["name"] = "Abdo"
        context["posts"] = Post.objects.all()
        return context
    
''' FBV for redirect
from django.shortcuts import redirect
def redirectToMosbat(request):
    return redirect('https://mosbatenergy.ir/')
'''

class RedirectToMosbat(RedirectView):

    
    url = 'https://mosbatenergy.ir/'


class PostListView(LoginRequiredMixin,ListView):
    #queryset = Post.objects.all()
    model = Post
    context_object_name = "posts"
    paginate_by = 3
    ordering = "id"


    #def get_queryset(self):
        #posts = Post.objects.filter(status=True)
        #return posts


class PostDetailView(DetailView):
    model = Post



'''class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = '/blog/post'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''


class PostCreateView(CreateView):
    model = Post
    #fields = ['author','title','content','status','category','published_date']
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post'



class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post'
