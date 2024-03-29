from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPortfolio(models.Model):
    user=models.OneToOneField(User,on_delete='SET_DEFAULT')
    portfolio=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
