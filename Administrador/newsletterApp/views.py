from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib import messages
# Create your views here.

from django.shortcuts import render

# Create your views here.

def inicio (request):
    return render(request, 'newsletterApp/index.html')

class postList(ListView):
    template_name = "newsletterApp/index.html"
    paginate_by = 4
    context_object_name = 'List_post'
    
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

class postDetail(DetailView):
    model = Post
    template_name = "newsletterApp/post_detail.html"


    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id) 
    
class postnew(CreateView):
    model = Post
    form_class= Post_form
    template_name = 'newsletterApp/post_form.html'
    success_url = reverse_lazy('inicio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA PUBLICACION '
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'post created successfully')
        return super().form_valid(form)    
    
class postUpdate (UpdateView):
    model = Post
    fields = ['title','tag','description','link','image']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)     

class postdelete(DeleteView):
    model = Post
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/post_delete.html'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The post has been deleted successfully.')
        return super().form_valid(form)  
    
