from django import forms
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    slug = models.SlugField(null=False,unique=True,db_index=True, blank=True, editable=False)


    def __str__(self):
        return f"{self.title}"
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
