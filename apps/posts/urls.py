from django.urls import path
from .views import (PostsApiView, PostDetailApiView,
                    PostCreateApiView, PostUpdateView,
                    PostDeleteApiView )

urlpatterns = [
    path("posts/", PostsApiView.as_view(), name="posts"),
    path("posts/<slug:slug>", PostDetailApiView.as_view(), name="detail"),
    path("posts/create/", PostCreateApiView.as_view(), name="create"),
    path("posts/edit/<slug:slug>/", PostUpdateView.as_view(), name="update"),
    path("posts/delete/<int:pk>/", PostDeleteApiView.as_view(), name="delete")

]
