from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

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

    
class tagList(ListView):
    template_name = "newsletterApp/list_tags.html"
    paginate_by = 4
    context_object_name = 'List_tags'
    
    def get_queryset(self):
        queryset = tags.objects.all()
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

class tagsnew(CreateView):
    model = tags
    form_class= tags_form
    template_name = 'newsletterApp/tags_form.html'
    success_url = reverse_lazy('new_tag')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA ETIQUETA'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'tag created successfully')
        return super().form_valid(form)   
    
class Commentnew(CreateView):
    model = Comment
    form_class= Comment_form
    template_name = 'newsletterApp/comment_form.html'
    success_url = reverse_lazy('inicio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA COMENTARIO'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'Comment created successfully')
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

class tagsUpdate (UpdateView):
    model = tags
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_tag')
        return tags.objects.get(id_tag=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)  

class commentUpdate (UpdateView):
    model = Comment
    fields = ['name','content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Comment.objects.get(id=kw_id) 

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

class tagsdelete(DeleteView):
    model = tags
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/tags_delete.html'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_tag')
        return Post.objects.get(id_tag=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The tag has been deleted successfully.')
        return super().form_valid(form)  

class tagsdelete(DeleteView):
    model = tags
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/tags_delete.html'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_tag')
        return tags.objects.get(id_tag=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The tag has been deleted successfully.')
        return super().form_valid(form)  

class commentdelete(DeleteView):
    model = Comment
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/comment_delete.html'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Comment.objects.get(id=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The comment has been deleted successfully.')
        return super().form_valid(form)  

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm (request, data = request.POST)
    
#         if form.is_valid():
            
#             data = form.cleaned_data
#             user = authenticate(username=data['username'], password=data['password'])
        
#             if user is not None :
#                 login(request, user)
#                 return render(request, "newsletterApp/index.html", {"mensaje" : f"Bienvenido {user.get_username()}" } )
#             else:
#                 return render (request, "newsletterApp/index.html", {"mensaje" : f"Usuario o Contraseña Incorrecta"} )
#         else:
#             return render(request, "newsletterApp/index.html", {"mensaje" : f"Error, formulario erroneo"} )
#     else:
#         form = AuthenticationForm()
#         return render (request, "newsletterApp/login.html", {'form':form})

