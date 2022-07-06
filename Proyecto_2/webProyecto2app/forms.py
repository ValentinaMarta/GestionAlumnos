from django.forms import ModelForm, EmailInput

from webProyecto2app.models import Alumno


class AlumnForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }