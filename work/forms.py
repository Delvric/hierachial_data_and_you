from django import forms
from file_system.models import File_System
from mptt.forms import TreeNodeChoiceField

class AddFilesForm(forms.Form):
    name = forms.CharField(max_length=40)
    parent = TreeNodeChoiceField(queryset=File_System.objects.all())