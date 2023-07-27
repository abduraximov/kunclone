from rest_framework import serializers
from .models import Post, Image


class PostSerializer(serializers.ModelSerializer):
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
            "images"
        )

    def get_images(self, obj):
        images = obj.image.all()
        if images:
            return list({str(image.image) for image in images})
