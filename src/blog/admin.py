from django.contrib import admin
from blog.models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'date_updated')

admin.site.register(BlogPost, BlogPostAdmin)