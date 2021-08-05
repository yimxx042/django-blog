from posts.validators import validate_symbols
from django import forms  
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        fields = ['title', 'content']   # if wants every form them '__all__'
        widgets = {'title': forms.TextInput(attrs={
            'class':'title',
            'placeholder':'Add Title'}),
            'content': forms.Textarea(attrs={
                'placeholder' : 'Add Content'})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('you can`t include the *.')
        return title 


