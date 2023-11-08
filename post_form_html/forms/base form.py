from django import forms
from post_form_html.models import *

class UpdatePostForm (forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].required=False
        self.fields['text'].required=False
        self.fields['counter'].required=False
    class Meta:
        model = PostForm
        fields = ['title','text','counter']
        