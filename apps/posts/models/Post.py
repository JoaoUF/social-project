from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user'
    )
    image = models.ImageField(
        db_column='image',
        upload_to='posts/%Y/%m/%d',
    )
    caption = models.TextField(
        db_column='caption',
        blank=True
    )
    title = models.CharField(
        db_column='title',
        max_length=200
    )
    slug = models.SlugField(
        db_column='slug',
        max_length=200,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'MAE_POST'
