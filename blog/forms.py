from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'project_text', 'project_member', 'project_extra',)