from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class full_form_categories(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.category

class full_form_data(models.Model):
    full_form_abbr=models.CharField(max_length=100)
    full_form=models.CharField(max_length=500)
    category=models.ForeignKey(full_form_categories,on_delete=models.CASCADE)
    content=RichTextUploadingField(blank=True)

    def __str__(self) -> str:
        return self.full_form_abbr






