from .Post import Post
from utils.model import Model
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Comment(ActivatorModel, TimeStampedModel, Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        db_column='post'
    )
    body = models.TextField(
        db_column='body'
    )

    class Meta:
        db_table = 'MAE_COMMENT'
        ordering = ('created',)
