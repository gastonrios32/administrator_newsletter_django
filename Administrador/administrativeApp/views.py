from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import memberform
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

# Create your views here.

def inicio (request):

    return render(request, 'administrativeApp/index.html')


class membersList(ListView):
    template_name = "administrativeApp/List_members.html"
    paginate_by = 5
    context_object_name = 'listMembers'
    
    def get_queryset(self):
        queryset = TlbMemberDetail.objects.select_related('id_member')
        return queryset

class memberDetail(DetailView):
    model = TlbMemberDetail
    template_name = "administrativeApp/member_detail.html"
    

# class membernew(CreateView):
#     model = TlbMembers
#     success_url = "../member_detail_new/"
#     fields=['id_member','member_name', 'status_memb' ]
    

class membernew(CreateView):
    model = TlbMembers
    form_class= memberform
    template_name = 'administrativeApp/TlbMembers_form.html'
    success_url = reverse_lazy('new_member_detail')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CREACION NUEVO MIEMBRO'
        return context

class memberdetailnew(CreateView):
    model = TlbMemberDetail
    success_url = "../members/"
    fields=['id_member','date_bith', 'direction', 'civil_status', 'dependents' ]