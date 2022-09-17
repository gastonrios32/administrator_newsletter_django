
from django import forms
from django.forms import ModelForm,widgets
from .models import TlbMembers, TlbMemberDetail,TlbMemberJob,tlb_member_phone,TlbMemberEmail

class memberform(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'
  
    class Meta:
            model = TlbMembers
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'member_name' : 'Nombre y Apellido', 'status_memb' : 'Estado' }
            
         

class memberdetailform(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'    
    class Meta:
            model = TlbMemberDetail
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'date_bith' : 'Fecha de Nacimiento' , 'direction' : 'Domicilio', 'civil_status' : 'Estado civil' ,  'dependents' : 'Personas a Cargo' }

class MemberJobform(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'
        
    class Meta:
            model = TlbMemberJob
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'id_position' : 'Puesto' , 'date_entry' : 'Fecha de Ingreso', 'direction' : 'Direccion Laboral' ,  'job_name' : 'Nombre de Empresa' }


class Memberphoneform(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'    
    class Meta:
            model = tlb_member_phone
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'phone1' : 'Numero' , 'type_phone' : 'Tipo', 'status_fone' : 'Estado del telefono'  }     

class MemberEmailform(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'
        self.fields['email'].widget.attrs['type'] = 'email'  
    class Meta:
            model = TlbMemberEmail
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'email' : 'Casilla de correo' }                                                                               