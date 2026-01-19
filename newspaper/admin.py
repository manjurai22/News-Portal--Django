from django.contrib import admin
from newspaper.models import Category, Post,Tag,Advertisement,Contact,OurTeam

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)