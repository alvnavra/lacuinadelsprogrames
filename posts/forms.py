from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':50,'class': 'form-control'}))

    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your comment',
        'id':'usercomment',
        'rows':'4'
    }))
    class Meta:
        model = Comment
        fields = ("content",)
