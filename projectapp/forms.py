from django.forms import ModelForm

from commentapp.models import Comment
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields= ['image','title','description']