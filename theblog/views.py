from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request,"home.html",{})
from .models import Post
from .forms import PostForm

from django.http import HttpResponse
from django.shortcuts import redirect


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm

    template_name = 'add_post.html'

    # fields = '__all__'
    # fields=("title","body")


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# def validate_view(request):
#     if request.method == 'POST':
#         form = AddPostView(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = AddPostView()
#     return render(request, 'add_post.html', {'form': form})
#
#
# def success(request):
#     return HttpResponse('successfully uploaded')
