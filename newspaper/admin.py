from django.contrib import admin
from newspaper.models import Category, Comment, Post,Tag,Advertisement,Contact,OurTeam, UserProfile, Newsletter
from tinymce.widgets import TinyMCE
# Register your models here.
from django import forms

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget = TinyMCE())

    class Meta:
        model = Post
        fields ="__all__"

from unfold.admin import ModelAdmin

@admin.register(Post)
class PostAdmin(ModelAdmin):
    form = PostAdminForm