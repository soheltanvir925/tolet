from django import forms
from .models import BlogPost, family_flat, bachalor_flat, Subscriber
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image','slug','date_post', 'latitude', 'longitude']  # Include the image field in the form
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class family_flat_Form(forms.ModelForm):
    image = forms.ImageField()  # Allow multiple images

    class Meta:
        model = family_flat
        fields = ['flat_owner','title','number_of_floor','total_number_of_room','number_of_masterbed','number_of_washroom','drowing_room','dining_room','price','phone_number','rent_date','address','location','images','lift_facility','gas_electric_bill_attach_with_price','gas_system']

class bachalor_flat_Form(forms.ModelForm):
    image = forms.ImageField()  # Allow multiple images

    class Meta:
        model = bachalor_flat
        fields = ['flat_owner','title','number_of_floor','number_of_room','number_of_seat','number_of_masterbed','price_per_seat','drowing_room','dining_room','price_per_room','phone_number','rent_date','address','location','images','lift_facility','gas_electric_bill_attach_with_price','gender','washroom_type','food_system']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']