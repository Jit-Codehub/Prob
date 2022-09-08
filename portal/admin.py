from django.contrib import admin
from .models import HomepageBlog
from django.utils.html import format_html

@admin.register(HomepageBlog)
class HomepageBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'updated_by',)
    search_fields = ("id", "app")
    list_filter = ("status",)
    list_display = ("app","app_url","status",)

    def app_url(self, obj):
        if obj.app=='':
            app_url='/'
        else:
            app_url = "/"+obj.app.replace("_","-")+"/"
        return format_html(f"<a href='{app_url}' target='_blank'>{app_url}</a>")

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.updated_by = request.user
        if change and obj.id:
            obj.updated_by = request.user
        obj.save()

