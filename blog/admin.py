from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'author', 'published_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

    # TODO: study the following properties and understand their relation
    # to the admin view 
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

admin.site.register(Post, PostAdmin)
# Register your models here.
