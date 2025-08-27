from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)
    slug=models.SlugField(default="", null=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_post=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(default="", null=False)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

class family_flat(models.Model):
    flat_owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default="TOLET")
    images=models.ImageField(upload_to='images/', null=False, blank=False)
    number_of_floor=models.IntegerField()
    total_number_of_room=models.IntegerField()
    number_of_masterbed=models.IntegerField()
    number_of_washroom=models.IntegerField()
    drowing_room=models.BooleanField()
    dining_room=models.BooleanField()
    lift_facility=models.BooleanField()
    GAS_CHOICES = [
        ('Cylinder Gas', 'Cylinder Gas'),
        ('Line Gas', 'Line Gas')
    ]
    gas_system = models.CharField(
        max_length=20,  # The length of 'M', 'F', or 'O' is 1 character
        choices=GAS_CHOICES,  # Use the GENDER_CHOICES defined above
        null=False, blank=False
    )

    gas_electric_bill_attach_with_price=models.BooleanField()
    price=models.IntegerField()
    phone_number=models.CharField(max_length=200, null=False, blank=False)
    rent_date=models.DateField(default=timezone.now)
    address=models.CharField(max_length=200, null=False, blank=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self) -> str:
        return f'{self.title} :Total room {self.total_number_of_room} from {self.rent_date}'

class bachalor_flat(models.Model):
    flat_owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default="TOLET")
    images=models.ImageField(upload_to='images/', null=False, blank=False)

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    gender = models.CharField(
        max_length=20,  # The length of 'M', 'F', or 'O' is 1 character
        choices=GENDER_CHOICES,  # Use the GENDER_CHOICES defined above
        null=False, blank=False
    )

    number_of_floor=models.IntegerField()
    number_of_room=models.IntegerField()
    number_of_seat=models.IntegerField()
    number_of_masterbed=models.BooleanField()
    lift_facility=models.BooleanField()
    gas_electric_bill_attach_with_price=models.BooleanField()
    washroom_CHOICES = [
        ('ATTACH', 'Attach'),
        ('COMMON', 'Common'),
    ]
    washroom_type = models.CharField(
        max_length=10,  # The length of 'M', 'F', or 'O' is 1 character
        choices=washroom_CHOICES,  # Use the GENDER_CHOICES defined above
        null=False, blank=False
    )
    FOOD_CHOICES = [
        ('Meal', 'Meal'),
        ('Fixed Meal', 'Fixed Meal'),
        ('Other System', 'Ohter System')
    ]
    food_system = models.CharField(
        max_length=20,  # The length of 'M', 'F', or 'O' is 1 character
        choices=FOOD_CHOICES,  # Use the GENDER_CHOICES defined above
        null=False, blank=False
    )
    drowing_room=models.BooleanField()
    dining_room=models.BooleanField()
    price_per_room=models.IntegerField(null=True, blank=True)
    price_per_seat=models.IntegerField(null=True, blank=True)
    phone_number=models.CharField(max_length=200, null=False, blank=False)
    rent_date=models.DateField(default=timezone.now)
    address=models.CharField(max_length=200, null=False, blank=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self) -> str:
        return f'{self.title} :Totel for {self.gender} from {self.rent_date} in {self.address}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email