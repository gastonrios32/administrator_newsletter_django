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

class membersList(ListView):
    template_name = "newsletterApp/index.html"
    paginate_by = 4
    context_object_name = 'List_post'
    
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset