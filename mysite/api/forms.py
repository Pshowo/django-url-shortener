from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    
    url_long = forms.URLField(widget=forms.URLInput())
    
    class Meta:
        model = Shortener
        fields = ('url_long',)