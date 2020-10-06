from django.contrib import admin
from .models import Post
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'creation_date', 'updation_date']
    list_display_links = ['creation_date', 'updation_date', 'title']
    list_filter = ['creation_date', 'updation_date']
    search_fields = ['title', 'content']
    ordering = ['title']


    



    class meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
