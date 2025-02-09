from django import forms
from .models import Comment, Contact_me

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'comment')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_me
        fields = ('email', 'subject', 'message')
