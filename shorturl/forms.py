from django import forms 
from .models import Shortner

class ShortnerFrom(forms.ModelForm):
    
    long_url=forms.URLField(widget=forms.URLInput(attrs={"class":"form-control form-control-lg","placeholder":"Your Url to short"}))
    
    class Meta:
        model = Shortner
        fields = ["long_url"]