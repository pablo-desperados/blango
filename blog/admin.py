from django.contrib import admin
from blog.models import Tag, Post

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    fields = ('slug','published_at')
admin.site.register(Post,PostAdmin)
