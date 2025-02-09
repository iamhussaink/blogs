from django.contrib import admin

# Register your models here.
from .models import Blogs, Comment , Contact_me

admin.site.register(Blogs)
admin.site.register(Comment)
admin.site.register(Contact_me)