from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy  as _

class UserManger(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('emial address' , unique=True)
    mobile_no = models.CharField(max_length=12)
    address = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManger()

    def __str__(self):
        return self.email

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehical_image = models.ImageField(upload_to='vehical')
    vehical_no = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    vehical_type = models.CharField(max_length=100)
    travel_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.owner_name

class Booking(models.Model):
    vehical = models.ForeignKey(Vehical, on_delete=models.CASCADE)   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
