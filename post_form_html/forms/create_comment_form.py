from django import forms
from post_form_html.models import *

class AddCommentForm (forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['text','status']