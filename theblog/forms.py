from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","title_tag","author","header_image") # took the body field out


        widgets ={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "title_tag ": forms.TextInput(attrs={"class": "form-control"}),
            #"author": forms.Select(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control","value":"" ,"id":"daniel","type":"hidden"}),
           ##"body": forms.Textarea(attrs={"class": "form-control"}),
        }
