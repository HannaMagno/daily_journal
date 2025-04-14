from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'mood', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }