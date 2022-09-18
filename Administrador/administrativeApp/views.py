from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import memberform,memberdetailform,MemberJobform,Memberphoneform,MemberEmailform
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

# Create your views here.

def inicio (request):

    return render(request, 'administrativeApp/index.html')


class membersList(ListView):
    template_name = "administrativeApp/List_members.html"
    paginate_by = 4
    context_object_name = 'listMembers'
    
    def get_queryset(self):
        queryset = TlbMemberDetail.objects.select_related('id_member')
        return queryset

class memberDetail(DetailView):
    model = TlbMemberDetail
    template_name = "administrativeApp/member_detail.html"

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberDetail.objects.get(id_member=kw_id) 
    
class memberDetail_job(DetailView):
    model = TlbMemberJob
    template_name = "administrativeApp/member_detail_job.html"

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberJob.objects.get(id_member=kw_id)       
    
class memberDetail_phone(DetailView):
    model = tlb_member_phone
    template_name = "administrativeApp/member_detail_phone.html"

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return tlb_member_phone.objects.get(id_member=kw_id)    
    
class memberDetail_email(DetailView):
    model = TlbMemberEmail
    template_name = "administrativeApp/member_detail_email.html"

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberEmail.objects.get(id_member=kw_id)            

#CREATE VIEW
    
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
    form_class= memberdetailform
    template_name = 'administrativeApp/TlbMemberDetail_form.html'
    success_url = reverse_lazy('new_member_detail')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS PERSONALES'
        return context



class MemberJobnew(CreateView):
    model = TlbMemberJob
    form_class= MemberJobform
    template_name = 'administrativeApp/TlbMemberJob_form.html'
    success_url = reverse_lazy('new_Member_Job')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS LABORALES'
        return context

class Memberphonenew(CreateView):
    model = tlb_member_phone
    form_class= Memberphoneform
    template_name = 'administrativeApp/TlbMemberPhone_form.html'
    success_url = reverse_lazy('new_Member_phone')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS DE CONTACTO'
        return context
    
class MemberEmailnew(CreateView):
    model = TlbMemberEmail
    form_class= MemberEmailform
    template_name = 'administrativeApp/TlbMemberEmail.html'
    success_url = reverse_lazy('new_Member_email')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS DE CONTACTO'
        return context    

