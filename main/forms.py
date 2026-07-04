from django.forms import ModelForm
from .models import Cliente

class ClienteForm():
    class Meta:
        model = Cliente
        fields = '__all__'