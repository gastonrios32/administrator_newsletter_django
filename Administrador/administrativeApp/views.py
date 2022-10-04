from datetime import datetime
from itertools import count
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import memberform,memberdetailform,MemberJobform,Memberphoneform,MemberEmailform
from .models import *
from django.views.generic import ListView,TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin,PermissionRequiredMixin


class LogoutIfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                return self.handle_no_permission()
            return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.



class membersList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "administrativeApp/List_members.html"
    paginate_by = 4
    context_object_name = 'listMembers'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = TlbMemberDetail.objects.select_related('id_member')
        return queryset

class memberDetailList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "administrativeApp/List_memberdetail.html"
    paginate_by = 4
    context_object_name = 'listMemberdetail'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = TlbMemberDetail.objects.select_related('id_member')
        return queryset   
    
class memberjobList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "administrativeApp/List_memberjob.html"
    paginate_by = 4
    context_object_name = 'listMemberjob'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = TlbMemberJob.objects.select_related('id_member')
        return queryset

class memberphoneList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "administrativeApp/List_memberphone.html"
    paginate_by = 4
    context_object_name = 'listMemberphone'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = tlb_member_phone.objects.select_related('id_member')
        return queryset

class memberemailList(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,ListView):
    template_name = "administrativeApp/List_memberemail.html"
    paginate_by = 4
    context_object_name = 'listMemberemail'
    permission_required = 'is_staff'
    
    def get_queryset(self):
        queryset = TlbMemberEmail.objects.select_related('id_member')
        return queryset   

class memberDetail(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DetailView):
    model = TlbMemberDetail
    template_name = "administrativeApp/member_detail.html"
    permission_required = 'is_staff'


    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberDetail.objects.get(id_member=kw_id) 
    
class memberDetail_job(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DetailView):
    model = TlbMemberJob
    template_name = "administrativeApp/member_detail_job.html"
    permission_required = 'is_staff'


    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberJob.objects.get(id_member=kw_id)      
    

    
class memberDetail_phone(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DetailView):
    model = tlb_member_phone
    template_name = "administrativeApp/member_detail_phone.html"
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return tlb_member_phone.objects.get(id_member=kw_id)    
    
class memberDetail_email(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DetailView):
    model = TlbMemberEmail
    template_name = "administrativeApp/member_detail_email.html"
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberEmail.objects.get(id_member=kw_id)            

#CREATE VIEW
    
class membernew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = TlbMembers
    form_class= memberform
    template_name = 'administrativeApp/TlbMembers_form.html'
    success_url = reverse_lazy('new_member_detail')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CREACION NUEVO MIEMBRO'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'Account created successfully')
        return super().form_valid(form)    

class memberdetailnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = TlbMemberDetail
    form_class= memberdetailform
    template_name = 'administrativeApp/TlbMemberDetail_form.html'
    success_url = reverse_lazy('new_member_detail')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS PERSONALES'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron cargados ')
        return super().form_valid(form)   

class MemberJobnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = TlbMemberJob
    form_class= MemberJobform
    template_name = 'administrativeApp/TlbMemberJob_form.html'
    success_url = reverse_lazy('new_Member_Job')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS LABORALES'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron cargados ')
        return super().form_valid(form)      

class Memberphonenew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = tlb_member_phone
    form_class= Memberphoneform
    template_name = 'administrativeApp/TlbMemberPhone_form.html'
    success_url = reverse_lazy('new_Member_phone')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS DE CONTACTO'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron cargados ')
        return super().form_valid(form)      
class MemberEmailnew(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,CreateView):
    model = TlbMemberEmail
    form_class= MemberEmailform
    template_name = 'administrativeApp/TlbMemberEmail.html'
    success_url = reverse_lazy('new_Member_email')
    permission_required = 'is_staff'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DATOS DE CONTACTO'
        return context    

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron cargados ')
        return super().form_valid(form)      

class MemberUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = TlbMembers
    fields = ['member_name','status_memb']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('members')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMembers.objects.get(id_member=kw_id) 

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)  
    
class MemberDetailUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = TlbMemberDetail
    fields = ['date_bith','direction','civil_status','dependents']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('member_detail_list')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMemberDetail.objects.get(id_member=kw_id)  

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)      
    
class MemberPhoneUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = tlb_member_phone
    fields = ['phone1','type_phone','status_fone']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('member_phone_list')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_contact')
        return tlb_member_phone.objects.get(id_contact=kw_id)     

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)           
    
class MemberJobUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = TlbMemberJob
    fields = ['id_position','date_entry','direction','job_name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('member_job_list')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('job_id')
        return TlbMemberJob.objects.get(job_id=kw_id)   

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)              
    
class MemberEmailUpdate (LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,UpdateView):
    model = TlbMemberEmail
    fields = ['email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('member_email_list')
    permission_required = 'is_staff'
    
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_email')
        return TlbMemberEmail.objects.get(id_email=kw_id)   

    def form_valid(self, form):
        messages.success(self.request, f'Los datos fueron actualizados ')
        return super().form_valid(form)            

class memberdelete(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DeleteView):
    model = TlbMembers
    success_url=reverse_lazy('members')
    template_name='administrativeApp/member_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_member')
        return TlbMembers.objects.get(id_member=kw_id)    
    
    def form_valid(self, form):
        messages.success(self.request, f'The member has been deleted successfully.')
        return super().form_valid(form)      
    
class memberJobdelete(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DeleteView):
    model = TlbMemberJob
    success_url=reverse_lazy('member_job_list')
    template_name='administrativeApp/member_job_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('job_id')
        return TlbMemberJob.objects.get(job_id=kw_id)  

    def form_valid(self, form):
        messages.success(self.request, f'The member has been deleted successfully.')
        return super().form_valid(form)        
class memberPhonedelete(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DeleteView):
    model = tlb_member_phone
    success_url=reverse_lazy('member_phone_list')
    template_name='administrativeApp/member_phone_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_contact')
        return tlb_member_phone.objects.get(id_contact=kw_id)  

    def form_valid(self, form):
        messages.success(self.request, f'The member has been deleted successfully.')
        return super().form_valid(form)        
    
    
class memberEmaildelete(LoginRequiredMixin,PermissionRequiredMixin, LogoutIfNotStaffMixin,DeleteView):
    model = TlbMemberEmail
    success_url=reverse_lazy('member_email_list')
    template_name='administrativeApp/member_email_delete.html'
    permission_required = 'is_staff'

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id_email')
        return TlbMemberEmail.objects.get(id_email=kw_id)    

    def form_valid(self, form):
        messages.success(self.request, f'The member has been deleted successfully.')
        return super().form_valid(form)                  

