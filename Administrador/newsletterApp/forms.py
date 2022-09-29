from django import forms
from django.forms import ModelForm,widgets
from .models import tags,Post,Comment

class Post_form(ModelForm):
    def __init__ ( self , * args , ** kwargs ):
        super().__init__ ( *args , **kwargs )
        for form in self.visible_fields ( ) :
            form.field.widget.attrs ['class'] = 'form-control'
            form.field.widget.attrs ['autocomplete '] = 'off'    
    class Meta:
            model = Post
            fields = '__all__'
            labels = {'title' : 'Titulo' , 'author' : 'Autor' , 'tag' : 'Etiqueta', 'description' : 'Descripcion' ,'link' : 'Enlace' , 'image' : 'Imagen de la publicacion' }     
