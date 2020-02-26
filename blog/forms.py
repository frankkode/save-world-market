from django import forms
from .models import Post
from django.contrib.auth.models import User

#post form
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'description',
            'price', 'image', 'phone', 'address', 'city', 'country')

#post edit form
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'description',
            'price', 'image', 'phone', 'address', 'city', 'country')

#contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)