from django.contrib import admin
from django import forms
from .models import Category, Article, Comment
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.register(Category)


# using CKEditor to create an article
class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


# add filter, search in admin panel
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created')
    list_filter = ('created', 'updated')


admin.site.register(Comment, CommentAdmin)
