from django.contrib import admin

from .models import Blogs, Categories, Comments

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class BlogsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'category', 'slug', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Categories, CategoryAdmin)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Comments, CommentAdmin)