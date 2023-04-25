from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet)
from users.views import UserCreateViewSet, UserReceiveJWTViewSet, UserViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='user')
router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')

router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/',
         UserCreateViewSet.as_view({'post': 'create'}),
         name='signup'),
    path(
        'v1/auth/token/',
        UserReceiveJWTViewSet.as_view({'post': 'create'}),
        name='token'),
]
