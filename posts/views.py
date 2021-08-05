from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all() #bring all data
    paginator = Paginator(posts, 6) #first parameter is data list for page, second paremeter is data list for one page
    curr_page_number = request.GET.get('page') #get how many pages from query string
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number) #get current page from pages
    return render(request, 'posts/post_list.html', {'page':page})
    


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)

# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
    
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'posts/post_form.html'


    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})
            

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})


def index(request):
    return redirect('post-list')