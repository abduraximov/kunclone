from django.shortcuts import render
from rest_framework import generics
from .serializer import (PostSerializer, PostDetailSerializer,
                         PostCreateSerializer, PostUpdateSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post


class PostsApiView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)


class PostDetailApiView(APIView):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post.views += 1
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=200)


class PostCreateApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


class PostDeleteApiView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
