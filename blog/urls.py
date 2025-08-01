from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/comments/', CommentListView.as_view(), name='comment-list'),
]
