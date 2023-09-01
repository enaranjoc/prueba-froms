from django import forms
from .models import *
from django.utils.html import format_html



class TaskForm(forms.ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'title': 'Titulo',
        } 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control '}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].label = format_html('<label class="text-danger fw-bold ">{}</label>', self.fields['title'].label)
    #     self.label_suffix = "" # Quitar los dos puntos del label ':' 

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = format_html('<label class="text-danger fw-bold ">{}</label>', self.fields[field_name].label)
        self.label_suffix = "" # Quitar los dos puntos del label ':'
        
        
