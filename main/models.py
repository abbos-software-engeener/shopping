from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
import os

from django.conf import settings

from shopping.helpers import UploadTo


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        self.phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_access_level', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo("Profile"))
    phone_number = models.CharField(unique=True, max_length=13, blank=True, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return os.path.join(settings.STATIC_URL, "img/no_avatar.jpg")


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    image1=models.ImageField()
    image2=models.ImageField(blank=True)
    image3=models.ImageField(blank=True)
    image4=models.ImageField(blank=True)
    image5=models.ImageField(blank=True)
    image6=models.ImageField(blank=True)
    image7=models.ImageField(blank=True)
    image8=models.ImageField(blank=True)
    image9=models.ImageField(blank=True)
    image10=models.ImageField(blank=True)
    image11=models.ImageField(blank=True)
    image12=models.ImageField(blank=True)
