from django.forms import model_to_dict
from rest_framework import mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from article.models import Article, Category
from .serializers import ArticleSerializer


class ApiViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Article.objects.all()[:3]

        return Article.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})