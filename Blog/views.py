from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# we don't use LoginRequiredMixin for restrict user to see post
class HomeView(ListView):
    model = Post 
    template_name = 'index.html'
    context_object_name = 'blog_entry'
    paginate_by = 3


@login_required(login_url='login')
def post_detail(request,post):
   
    post = get_object_or_404(Post, slug=post)
                                
    return render(request, 'post_detail.html', {'post':post})



class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ('title','body',)
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class POSTUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = [ 'title',
                'body' ]
    template_name = 'post_form.html'
    success_url = "/"

class POSTDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url ="/"


def search(request):
    query = request.GET['search_query']
    if len(query) > 60:
        blog_entry  = Post.objects.none()
    else:
        blog_entry = Post.objects.filter(title__icontains=query)

        context = {'blog_entry':blog_entry,
                    'query':query}

    return render(request, 'search_show.html', context)






