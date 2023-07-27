from django.shortcuts import render

from .serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post


class PostsApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)


class PostDetailApiView(APIView):

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)

