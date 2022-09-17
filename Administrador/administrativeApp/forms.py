from cProfile import label
from django.forms import ModelForm
from .models import TlbMembers

class memberform(ModelForm):
    class Meta:
            model = TlbMembers
            fields = '__all__'
            labels = {'id_member' : 'DNI' , 'member_name' : 'Nombre y Apellido' }
            