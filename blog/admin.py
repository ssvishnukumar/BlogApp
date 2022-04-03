# Register your models here.
from django.contrib import admin
from .models import *

# below are the fields that we see in the admin panel. Just making it for better looking.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)