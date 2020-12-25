from .models import Comment,Book
from django import forms


class CommentForm(forms.ModelForm): 
    content = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':4, 
        'cols':50
    })) 
    class Meta: 
        model = Comment 
        fields =['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'tags'
        ]
