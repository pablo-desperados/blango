from django.contrib import admin
from blog.models import Tag, Post, Comment

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    fields = ('author','published_at','title','slug','summary','content')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
