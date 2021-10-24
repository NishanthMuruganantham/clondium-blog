from django import forms
from .models import Post, Comment, Reply


class PostCreationForm(forms.ModelForm):
    class Meta:
        fields = ['title','short_description','content','header_image','category','tags']
        model = Post
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'your title',
                                                                'class':'input--style-6'}),
            'short_description': forms.Textarea(attrs={'placeholder':'Give a short description about your post in minimum of 250 characters and maximum of 300 characters',
                                            'class':'form-control','minlength':50}),
            'content': forms.Textarea(attrs={'placeholder':'put your content here...',
                                            'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'custom-select'}),
            # 'header_image': forms.ClearableFileInput(attrs={'class':'input-file'})
            'tags': forms.TextInput(attrs={'placeholder':'your tags',
                                                                'class':'input--style-6',
                                                                'data-role':'tagsinput'}),
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


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-input','rows': 6, 'cols':'100px'})
        }