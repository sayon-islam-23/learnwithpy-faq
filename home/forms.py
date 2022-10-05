from django import forms
from .models import Profile, BlogPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('query', 'tagline', 'details', 'image')
        widgets = {
            'query': forms.TextInput(attrs={'class':'form-control', 'placeholder':'type your question'}),
            'tagline': forms.TextInput(attrs={'class':'form-control', 'placeholder':'unique tagline without any space (or separated by _)'}),
            'details': forms.Textarea(attrs={'class':'form-control', 'placeholder':'write your doubt in details'}),
        }