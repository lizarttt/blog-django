from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]


router = MyCustomRouter()
router.register(r'api', ApiViewSet, basename='api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  #     api db article - http://127.0.0.1:8000/api/v1/api or one object http://127.0.0.1:8000/api/v1/api/1
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('article.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]
