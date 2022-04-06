from django import forms
from .models import Post
from .perceptual import dhash
from PIL import Image


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

    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()

        # extract the username and text field from the data
        header_image = self.cleaned_data.get('header_image')
        author =self.cleaned_data.get("author")

        # the dhash checks the images by calculating the hamming distance
        if not (dhash.check_perceptual(header_image)): # If not True(means same pic) the error is thrown and the function stops
            self._errors['header_image'] = self.error_class([
                'The picture is too similar to existing picture in the website'])

        # return any errors if found
        return self.cleaned_data
