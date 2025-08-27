from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<slug:slug>/', views.blog_details, name='blog_details'),
    path('service/', views.service, name='service'),
    path('room/', views.room, name='room'),
    path('room_details/<int:id>/', views.room_details, name='room_details'),
    path('booking/', views.booking, name='booking'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('create_post/', views.create_post, name='create_post'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)