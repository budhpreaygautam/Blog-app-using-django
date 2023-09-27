from django.contrib import admin

from .models import Category, Post, BlogComment


# Register your models here.

# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'add_date', 'image_tags')
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10


# for configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image_tags')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js', 'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)
