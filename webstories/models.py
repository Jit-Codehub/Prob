from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class web_stories_data(models.Model):
    title=models.CharField(max_length=1000)
    content=RichTextUploadingField(blank=True)
