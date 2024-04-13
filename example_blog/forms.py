from django_summernote.widgets import (
    SummernoteWidget,
    SummernoteInplaceWidget
)
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import BlogPost as Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget()
        }

