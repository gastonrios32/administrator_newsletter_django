from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,widgets
from django.contrib.auth.models import User
from django import forms
from .models import tags,Post,Comment,events_calendar

class Post_form(ModelForm):
    
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off' 
        
    class Meta:
            model = Post
            fields = ['title','tag','description','link','image']
            labels = {'title' : 'Titulo' , 'author' : 'Autor' , 'tag' : 'Etiqueta', 'description' : 'Descripcion' ,'link' : 'Enlace' , 'image' : 'Imagen de la publicacion' }     

class tags_form(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'    
    class Meta:
            model = tags
            fields = '__all__'
            labels = {'name' : 'Nombre de la etiqueta' }     

class Comment_form(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'
    class Meta:
            model = Comment
            fields = ['post','name','content']
            
            labels = {'post' : 'Post' , 'name' : 'Nombre y Apellido' , 'content' : 'Contenido'  } 
            
class Calendar_form(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'
    class Meta:
            model = events_calendar
            fields = ['title','date_start','date_end']
            
            labels = {'title' : 'Titulo' , 'date_start' : 'Fecha de inicio' , 'date_end' : 'Fecha de fin'  } 

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label= "Modificar Email")
    password1 = forms.CharField(label= "Contrase??a",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contrase??a",widget=forms.PasswordInput)
    last_name = forms.CharField(label= "Ingrese su Apellido")
    first_name = forms.CharField(label= "Ingrese su Nombre")
    
    class Meta:
        model = User
        fields = ['email','password1','password2','last_name','first_name']
        help_texts = {k:"" for k in fields}  
        
class UserregisterForm(UserCreationForm):
    pass