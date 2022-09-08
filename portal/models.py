from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

APP_NAME_CHOICE = (
    ("full-form", "full forms"),
    ("probability", "Probability"),
    ("web-stories", "webstory")
)
STATUS_CHOICE = (("Draft", "Draft"), ("Published", "Published"))

class HomepageBlog(models.Model):
    app = models.CharField(max_length=50,unique=True,choices=APP_NAME_CHOICE,verbose_name = "APP Name")
    title = models.CharField(max_length=500, null=True, blank=True)
    main_content = RichTextUploadingField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="Draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="homepage_blog_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="homepage_blog_updated_by")
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.app