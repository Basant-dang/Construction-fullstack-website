from django import forms
from .models import Project,Document

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client_name', 'description', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'end_date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'})
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'description']