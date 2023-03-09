from django.contrib import admin
from .models import Comments


# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_com', 'email_com', 'post_com', 'date_com', 'published_com')
    list_display_links = ('id', 'name_com', 'email_com')
    list_filter = ('published_com', 'date_com')
    search_fields = ('name_com', 'email_com', 'comment')
    list_editable = ('published_com',)
    date_hierarchy = 'date_com'
    ordering = ('published_com', 'date_com')


admin.site.register(Comments, CommentsAdmin)
