from django.contrib import admin
from announce.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'date_updated')

admin.site.register(BlogPost, BlogPostAdmin)