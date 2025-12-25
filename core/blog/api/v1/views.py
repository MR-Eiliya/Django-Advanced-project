from rest_framework.permissions import (
    IsAuthenticated
)
from .serializers import PostSerializers, CategorySerializer
from ...models import Post, Category
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


# viewset example for cbv
class PostModelViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["=title"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
