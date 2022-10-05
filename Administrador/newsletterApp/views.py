from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView,TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin,PermissionRequiredMixin
# Create your views here.

from django.shortcuts import render

# Create your views here.

def inicio (request):
    return render(request, 'newsletterApp/index.html')

class LogoutIfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                return self.handle_no_permission()
            return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

class postList(ListView):
    template_name = "newsletterApp/index.html"
    paginate_by = 4
    context_object_name = 'List_post'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-create_at')
        return queryset

class postListimportant(ListView):
    template_name = "newsletterApp/List_post_Important.html"
    paginate_by = 4
    context_object_name = 'List_post_important'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = Post.objects.all().filter(is_important='True').order_by('-create_at')
        return queryset

    
class tagList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "newsletterApp/list_tags.html"
    paginate_by = 4
    context_object_name = 'List_tags'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = tags.objects.all()
        return queryset

class CalendarPage(TemplateView):
    template_name = 'newsletterApp/calendar.html'
    form_class = Calendar_form

    def get_context_data(self, **kwargs):
        context = super(CalendarPage, self).get_context_data(**kwargs)
        context['eventlist'] = events_calendar.objects.all()
        return context


class eventsList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "newsletterApp/list_events.html"
    paginate_by = 10
    context_object_name = 'List_events'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = events_calendar.objects.all().order_by('-date_start')
        return queryset

class postDetail(DetailView):
    model = Post
    template_name = "newsletterApp/post_detail.html"
    permission_required = 'is_staff'


    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id) 
    
class postnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = Post
    form_class= Post_form
    template_name = 'newsletterApp/post_form.html'
    success_url = reverse_lazy('inicio')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA PUBLICACION '
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, f'post created successfully')
        return super().form_valid(form) 


class tagsnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = tags
    form_class= tags_form
    template_name = 'newsletterApp/tags_form.html'
    success_url = reverse_lazy('new_tag')
    permission_required = 'is_staff'
    
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
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA COMENTARIO'
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, f'Comment created successfully')
        
        return super().form_valid(form) 

class eventnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = events_calendar
    form_class= Calendar_form
    template_name = 'newsletterApp/events_form.html'
    success_url = reverse_lazy('Calendar_events')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO EVENTO'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'Event created successfully')
        return super().form_valid(form)   
class postUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = Post
    fields = ['title','tag','description','link','image','is_important']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form) 

class tagsUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = tags
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')
    permission_required = 'is_staff'
    
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
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Comment.objects.get(id=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form) 

class eventUpdate (UpdateView):
    model = events_calendar
    fields = ['title','date_start','date_end']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('Calendar_events')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return events_calendar.objects.get(id=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form) 

class postdelete(DeleteView):
    model = Post
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/post_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_post')
        return Post.objects.get(id_post=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The post has been deleted successfully.')
        return super().form_valid(form)  

class tagsdelete(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DeleteView):
    model = tags
    success_url=reverse_lazy('inicio')
    template_name='newsletterApp/tags_delete.html'
    permission_required = 'is_staff'

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
    permission_required = 'is_staff'

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
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Comment.objects.get(id=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The comment has been deleted successfully.')
        return super().form_valid(form)  

class eventsdelete(DeleteView):
    model = events_calendar
    success_url=reverse_lazy('Calendar_events')
    template_name='newsletterApp/events_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return events_calendar.objects.get(id=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The tag has been deleted successfully.')
        return super().form_valid(form)  

def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miform= UserEditForm(request.POST)
        if miform.is_valid():
            
            informacion = miform.cleaned_data
            
            usuario.email= informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion ['first_name']
            usuario.save()
            
            return render (request, "newsletterApp/index.html", {"mensaje" :"Usuario Modificado  "})
    else:
        miform = UserEditForm(initial={'email':usuario.email,'first_name':usuario.first_name, 'last_name': usuario.last_name })
        
    return render (request, "newsletterApp/editarPerfil.html", {"miform":miform,"usuario":usuario})



class register(CreateView):
    model = User
    form_class= UserregisterForm
    template_name = 'newsletterApp/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, f'User created successfully')
        return super().form_valid(form) 