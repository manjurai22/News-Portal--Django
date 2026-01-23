from django.contrib import admin
from newspaper.models import Category, Comment, Post,Tag,Advertisement,Contact,OurTeam, UserProfile, Newsletter

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)