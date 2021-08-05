from django import forms
from .models import Post, Comment


class PostCreationForm(forms.ModelForm):
    class Meta:
        fields = ['title','content','header_image','category']
        model = Post
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'your title',
                                                                'class':'input--style-6'}),
            'content': forms.Textarea(attrs={'placeholder':'put your content here...',
                                            'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'custom-select'}),
            # 'header_image': forms.ClearableFileInput(attrs={'class':'input-file'})
        }
        
        help_texts = {
            'title' : "-title here"
        }
        
        labels = {
            'title' : 'Blog Title'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['header_image'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-input','rows': 6, 'cols':'100px'})
        }