from django import forms
from .models import LugarPatrimonial


class LugarForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'imagen', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for nombre, campo in self.fields.items():
            campo.widget.attrs['class'] = 'form-select' if nombre == 'categoria' else 'form-control'