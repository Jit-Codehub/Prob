from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS_CHOICE = (("Draft", "Draft"), ("Published", "Published"))

class Blog(models.Model):
    title = models.CharField(max_length=500, unique=True)
    url_slug = models.SlugField(max_length=500, unique=True)
    content = RichTextUploadingField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="Draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guides_blog_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guides_blog_updated_by")
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    extra_script_tags = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.url_slug)
        print(*args,**kwargs)
        super(Blog, self).save(*args, **kwargs)