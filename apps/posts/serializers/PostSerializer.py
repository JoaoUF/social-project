from rest_framework import serializers
from apps.posts.models import Post
from django.utils.text import slugify


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, data):
        post = Post.objects.create(**data)
        post.slug = slugify(post.title)
        post.save()
        return post
