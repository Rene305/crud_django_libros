from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'fecha_publi', 'cover_image']
        labels = {
            'title':'Titulo',
            'author':'Autor',
            'fecha_publi':'Fecha de Publicacion (MM/DD/AA)',
            'cover_image':'cover_image',
        }

class BookImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['fecha_publi','cover_image']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'})
        }
        