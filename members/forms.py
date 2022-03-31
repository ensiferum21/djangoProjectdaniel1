from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from theblog.models import Profile
from theblog.models import models
import os
from django.conf import settings
from .recognition import compare_faces

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=("profile_pic","user","clear")
        profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")


        widgets={
           # "profile_pic": forms.TextInput(attrs={"class": "form-control"}),
            "user": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "daniel", "type": "hidden"}),
            "clear":forms.CheckboxInput()
        }
    def clean(self):

        # data from the form is fetched using super function
        super(ProfilePageForm, self).clean()

        profile_pic=self.cleaned_data.get("profile_pic")
        user= self.cleaned_data.get('user')

        if profile_pic == False:
            if (self.cleaned_data.get("clear") == True):
                try:
                    for file in Profile.objects.all():
                        if user == file.user:
                            os.remove(os.path.join(settings.BASE_DIR,file.profile_pic.url[1:len(file.profile_pic.url.replace("/","\\"))]))
                            file.profile_pic="static/theblog/images/Default_profile.jpg"

                except:
                    self.errors['profile_pic']=self.error_class(["Error Occured"])

        if profile_pic != False:
            for file in Profile.objects.all():
                if user==file.user:
                    # if file.profile_pic == profile_pic:
                    #     self._errors['profile_pic'] = self.error_class([
                    #         "You're not uploading a valid picture!"])
                    #     break
                    if(self.cleaned_data.get("clear") == True and file.profile_pic == profile_pic):

                        file.set_default()
                        self.errors['profile_pic'] = self.error_class(["Profile picture has been cleared (pls refresh the page)"])

                        break



                    # try:
                    #     os.remove(os.path.join(settings.BASE_DIR,file.profile_pic.url[1:len(file.profile_pic.url.replace("/","\\"))]))
                    #
                    # except ValueError:
                    #     0


                    if (compare_faces(profile_pic)==IndexError):
                        self._errors['profile_pic']=self.error_class(["Please upload picture of a face!"])
                        break

                    elif not (compare_faces(profile_pic)):
                        self._errors['profile_pic'] = self.error_class([
                        'The profile picture is too similar to existing profile picture in the website'])


            # return any errors if found
        return self.cleaned_data


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

