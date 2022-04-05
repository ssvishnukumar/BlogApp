from django import forms
from blog.models import *



class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','content','author','status',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between (slug)'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'type':'hidden',  'id':'id_num', }), # here after , we have to create a small javascript code in add_blog.html ... # here, 'id':'id_num' is created to make the reference to the java script code.
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'''Write Your Content Here.
Note: You Can't Edit Once Created.'''}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
