from django import forms
# from posts.models import *

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as __
from django import forms

# class UpdatePostForm (forms.ModelForm):
#     def __init__(self, *args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['title'].required=False
#         self.fields['text'].required=False
#         self.fields['counter'].required=False
#     class Meta:
#         model = Post
#         fields = ['title','text','counter']
        
class UpdatePostForm (forms.Form):
    title = forms.CharField(max_length=100,required=False)
    text = forms.CharField(required=False)
    counter = forms.IntegerField(required=False)

    def clean_counter(self):
        if self.cleaned_data ['counter'] > 20:
            raise ValidationError (__(f"Price is {self.cleaned_data['counter']}, should be not more than 20"))

    
    def clean(self) -> dict[str,any]:
        return super().clean()
    
