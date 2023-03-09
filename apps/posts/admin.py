from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_post', 'author_post', 'date_posted_post', 'category_post', 'published_post')
    list_display_links = ('id', 'title_post', 'author_post')
    search_fields = ('title_post', 'content_post')
    list_filter = ('author_post', 'category_post')
    list_editable = ('published_post',)
    list_per_page = 10


admin.site.register(Post, PostAdmin)
