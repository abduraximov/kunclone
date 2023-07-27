from rest_framework import serializers
from .models import Post, Image
import math


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField("get_images")
    time_to_read = serializers.SerializerMethodField("to_read")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "video_link",
            "region",
            "category",
            "tag",
            "is_recommend",
            "is_active",
            "images",
            "created_at",
            "time_to_read"
        )

    def get_images(self, obj):
        images = obj.image.all()
        if images:
            return list({str(image.image) for image in images})

    def to_read(self, obj):
        content = str(obj.content).split()
        return math.ceil(len(content) / 200)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "content",
            "video_link",
            "region",
            "category",
            "tag",
            "is_recommend",
            "is_active",
            "image",
        )

    def create(self, validate_data):
        image = validate_data.pop("image")
        tags_data = validate_data.pop("tag")
        post = Post.objects.create(**validate_data)
        Image.objects.create(name=validate_data['title'], image=image, post=post)
        post.tag.set(tags_data)
        return post


class PostDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField("get_images")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "video_link",
            "region",
            "category",
            "tag",
            "is_recommend",
            "is_active",
            "views",
            "images",
            "created_at"
        )

    def get_images(self, obj):
        images = obj.image.all()
        if images:
            return list({str(image.image) for image in images})


class PostUpdateSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField("get_images")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "video_link",
            "region",
            "category",
            "tag",
            "is_recommend",
            "is_active",
            "images",
        )

    def get_images(self, obj):
        images = obj.image.all()
        if images:
            return list({str(image.image) for image in images})