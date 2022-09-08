from django.contrib import admin
from .models import Blog
from django.utils.html import format_html

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'updated_by',"created_at","updated_at")
    search_fields = ("id", "title", "url_slug")
    list_filter = ("status",)
    list_display = ("title","blog_url","status")

    def blog_url(self, obj):
        url = "/guide/"+obj.url_slug+"/"
        return format_html(f"<a href='{url}' target='_blank'>{url}</a>")

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.updated_by = request.user
        if change and obj.id:
            obj.updated_by = request.user
        obj.save()
