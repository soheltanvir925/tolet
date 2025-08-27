from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import SubscriberForm, UserRegisterForm,BlogPostForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def members(request):
    mymembers= Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymember=Member.objects.get(slug=slug)
    template=loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers=Member.objects.all().order_by('firstname','-slug').values
    template=loader.get_template('template.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  # Show a thank you page
    else:
        form = SubscriberForm()

    bachalor_posts = bachalor_flat.objects.all().order_by('-rent_date')
    posts=BlogPost.objects.all().order_by('-date_post')
    rooms=family_flat.objects.all().order_by('-rent_date')
    template=loader.get_template('index.html')
    context = {
        'posts':posts,
        'rooms':rooms,
        'b_room':bachalor_posts,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Use Django's send_mail function to send the email
        send_mail(
            subject=f'New contact form submission: {subject}',
            message=f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['soheltanvrir925@gmail.com'],
            fail_silently=False,
            #auth token: vdxg qaom acuy ibhv
        )

        # You can add a success message or redirect here
        return render(request, 'contact.html', {'success_message': 'Your message has been sent successfully!'})
        #return render(request, 'contact.html', {'message_sent': True})

    return render(request, 'contact.html', {'message_sent': False})
    #return render(request, 'contact.html', {})

def booking(request):
    template=loader.get_template('booking.html')
    return HttpResponse(template.render())

def testimonial(request):
    template=loader.get_template('testimonial.html')
    return HttpResponse(template.render())

def team(request):
    template=loader.get_template('team.html')
    return HttpResponse(template.render())

def blog(request):
    posts=BlogPost.objects.all().order_by('-date_post')
    template=loader.get_template('blog.html')
    context = {
        'posts':posts,
    }
    return HttpResponse(template.render(context, request))

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.user = request.user
            user_post.save()
            return redirect('index.html')  # Redirect to a success page
    else:
        form = BlogPostForm()
    return render(request,'create_post.html', {'form': form})

def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_details.html', {'post': post})

def service(request):
    template=loader.get_template('service.html')
    return HttpResponse(template.render())

def room(request):
    rooms=family_flat.objects.all().order_by('-rent_date')
    template=loader.get_template('room.html')
    context={
        'rooms': rooms,
    }
    return HttpResponse(template.render(context, request))

def room_details(request, id):
    details=family_flat.objects.get(id=id)
    template=loader.get_template('room_details.html')
    context={
        'room': details
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            # Validate email
            validate_email(email)
            # Here, save email to your database or mailing list
            # Example:
            # NewsletterSubscriber.objects.create(email=email)
            
            return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing!'})
        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Please enter a valid email address.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('index')