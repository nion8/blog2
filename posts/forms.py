from django import forms
from .models import *


#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = [""]

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows: 2', 'cols: 80'}), max_length=300)
