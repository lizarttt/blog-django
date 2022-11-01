from django.db import models
from user.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        null=True,
    )
    image = models.ImageField(
        upload_to='image/',
        default='0',
    )
    name = models.CharField(
        verbose_name='Название статьи',
        max_length=80,
    )
    description = models.TextField(
        verbose_name='Информация статьи',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
    )

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    post = models.ForeignKey(
        Article,
        related_name='comment_article',
        on_delete=models.PROTECT,
        null=True,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.PROTECT,
        null=True,
        default=User
    )
    body = models.TextField(
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'