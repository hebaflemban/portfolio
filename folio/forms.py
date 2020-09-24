from django import forms
from .models import Project, Guest, Tag

class ContactForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

# 
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = '__all__'
#         widgets = { 'tags': forms.CheckboxSelectMultiple }
#
#
# class TagsForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = "__all__"
