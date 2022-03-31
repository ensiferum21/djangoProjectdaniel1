from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title+"|"+str(self.author)

    def get_absolute_url(self):
        return reverse("home")


class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,upload_to="images/profile/")
    clear = models.BooleanField(default=False)

    def set_default(self):
        print(self.profile_pic)
        if(self.profile_pic !="static/Default_profile.jpg"):
            self.profile_pic.delete(save=True)
        print(self.profile_pic)
        self.profile_pic="static/Default_profile.jpg"
        self.save()
        print(self.profile_pic)
        print(self.profile_pic.url)
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")
