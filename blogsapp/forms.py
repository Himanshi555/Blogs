from django import forms
from . models import Blog, Comment

class blogform(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('Name','comment', )
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here!!!!','rows':'4','cols':'50'})
                  }
