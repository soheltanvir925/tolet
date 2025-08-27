from django.contrib import admin
from .models import Member, BlogPost, family_flat, bachalor_flat, Subscriber
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(Member, MemberAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_post']
    fields = ['title', 'content', 'author', 'image','slug','date_post']
    prepopulated_fields={"slug":("title", "author")}

admin.site.register(BlogPost, BlogPostAdmin)

class family_flat_Admin(admin.ModelAdmin):
    list_display = ['flat_owner','title', 'total_number_of_room', 'rent_date','address','phone_number']

admin.site.register(family_flat, family_flat_Admin)

class bachalor_flat_Admin(admin.ModelAdmin):
    list_display = ['flat_owner','title', 'number_of_room', 'rent_date','address','phone_number']
admin.site.register(bachalor_flat, bachalor_flat_Admin)

admin.site.register(Subscriber)