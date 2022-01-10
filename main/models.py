from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
import os
from django.conf import settings
from shopping.helpers import UploadTo


class UserManager(BaseUserManager):

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

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo("Profile"))
    username = None
    email = None
    phone = models.CharField(unique=True, max_length=13, blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return os.path.join(settings.STATIC_URL, "img/no_avatar.jpg")


class Category(models.Model):
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='category/')
    image2 = models.ImageField(blank=True, upload_to='category/')
    image3 = models.ImageField(blank=True, upload_to='category/')
    image4 = models.ImageField(blank=True, upload_to='category/')
    image5 = models.ImageField(blank=True, upload_to='category/')
    image6 = models.ImageField(blank=True, upload_to='category/')
    image7 = models.ImageField(blank=True, upload_to='category/')
    image8 = models.ImageField(blank=True, upload_to='category/')
    image9 = models.ImageField(blank=True, upload_to='category/')
    image10 = models.ImageField(blank=True, upload_to='category/')
    image11 = models.ImageField(blank=True, upload_to='category/')
    image12 = models.ImageField(blank=True, upload_to='category/')


class Pans(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pans/')
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)


class Payment(models.Model):
    CHOICES = (
        (1, 'NAQD'),
        (2, 'Karta')
    )
    pay_method = models.CharField(max_length=100, choices=CHOICES)
    address = models.CharField(max_length=255)

