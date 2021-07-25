from django.db import models

# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=255,)
    bio=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,)
    address=models.TextField(max_length=1000,)
    phonenumber=models.CharField(max_length=20)
    profileimage=models.ImageField(upload_to='profileimage')

    def __str__(self):
        return self.username


class SocialDetails(models.Model):
    friends=models.ManyToManyField(Profile,on_delete=models.CASCADE)
    posts=models.ManyToManyField(Profile,on_delete=models.CASCADE)

