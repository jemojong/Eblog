from django import forms
from .models import Thoughts

class ThoughtsForm(forms.ModelForm):
    class Meta:
        model= Thoughts
        exclude =["article"]
        labels = {
            "user":"Your Name",
            "email":"Your Email",
            "text":"Your Thougths"
        }
