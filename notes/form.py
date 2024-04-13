

from django import forms
from django.core.exceptions import ValidationError
from .models import notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['title', 'text']

        def clean_title(self):
           title = self.clean_data['title']
           if 'django' not in title:
                raise ValidationError("Title must contain 'django'.")
           return title



