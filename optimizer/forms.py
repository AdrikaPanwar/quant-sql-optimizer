from django import forms
from .models import SQLFile

class SQLFileForm(forms.ModelForm):
    class Meta:
        model = SQLFile
        fields = ['uploaded_file']
