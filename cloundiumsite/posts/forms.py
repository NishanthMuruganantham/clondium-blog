from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        fields = ['title','content','header_image','category']
        model = Post
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'your title',
                                                                'class': 'input100'}),
            'content': forms.Textarea(attrs={'placeholder':'put your content here...',
                                            'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-2'})
        }
        
        help_texts = {
            'title' : "-title here"
        }
        
        labels = {
            'title' : 'Blog Title'
        }
