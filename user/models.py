from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

#In user we have created profile model

# Create your models here.
class Profile(models.Model):  # relationship with User model
    staff = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)],null=True)
    image = models.ImageField(default='default.jpg', upload_to='Profile_images')

    def __str__(self) -> str:
        return f'{self.staff.username}'