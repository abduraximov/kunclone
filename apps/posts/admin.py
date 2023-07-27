from django.contrib import admin
from .models import Post, Region, Category, Image, Tag


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, ArticleAdmin)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Tag)


