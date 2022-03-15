from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from theblog.models import Profile
from theblog.models import models


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=("profile_pic",)
        profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

        widgets={
           # "profile_pic": forms.TextInput(attrs={"class": "form-control"}),

        }


class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))


    class Meta:
        model=User
        fields =("username","first_name","last_name","email","password1","password2")

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs["class"]="form-control"
        self.fields['password1'].widget.attrs["class"]="form-control"
        self.fields['password2'].widget.attrs["class"]="form-control"


class EditProfileForm(UserChangeForm):
    password = None
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=("email",)

