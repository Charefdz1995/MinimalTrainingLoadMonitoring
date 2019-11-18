from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager
from .choices import NATIONALITIES

class CustomUser(AbstractUser):
    username = None 
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()


    def __str__(self):
        return "{}".format(self.email)


class Profile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length = 45 , choices = NATIONALITIES)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(default = 'default_pic.png', upload_to = "profile_pics")