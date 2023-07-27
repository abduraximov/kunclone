from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Region(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.CharField(max_length=256)
    content = RichTextField()
    video_link = models.CharField(max_length=256, null=True, blank=True)
    region = models.ForeignKey("posts.Region",
                               on_delete=models.CASCADE,
                               related_name="post",
                               verbose_name=_("Region"))
    category = models.ForeignKey("posts.Category",
                                 on_delete=models.CASCADE,
                                 related_name="post",
                                 verbose_name=_("Category"))

    tag = models.ManyToManyField("posts.Tag", related_name="post", verbose_name=_("Tags"))
    is_recommend = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(BaseModel):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    post = models.ForeignKey("posts.Post",
                             on_delete=models.CASCADE,
                             related_name="image",
                             verbose_name=_("Post"))

    def __str__(self):
        return self.name
