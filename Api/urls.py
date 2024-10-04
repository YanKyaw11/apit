from django.urls import path
from .views import category_views, video_views, comment_views,reply_views

urlpatterns = [
    # Category URLs
    path('categories/', category_views.category_list, name='category-list'),
    path('categories/create/', category_views.category_create, name='category-create'),
    path('categories/<int:pk>/', category_views.category_detail, name='category-detail'),
    path('categories/<int:pk>/update/', category_views.category_update, name='category-update'),
    path('categories/<int:pk>/delete/', category_views.category_delete, name='category-delete'),
    path('categories/<int:pk>/videos/', category_views.category_videos, name='category-videos'),
    

    # Video URLs
    path('videos/', video_views.video_list, name='video-list'),
    path('videos/create/', video_views.video_create, name='video-create'),
    path('videos/<int:pk>/', video_views.video_detail, name='video-detail'),
    path('videos/<int:pk>/update/', video_views.video_update, name='video-update'),
    path('videos/<int:pk>/delete/', video_views.video_delete, name='video-delete'),

    # Comment URLs
    path('comments/', comment_views.comment_list, name='comment-list'),
    path('comments/create/', comment_views.comment_create, name='comment-create'),
    path('comments/<int:pk>/', comment_views.comment_detail, name='comment-detail'),
    path('commentsfilter/<int:pk>/', comment_views.comment_filter, name='comment-filter'),
    path('comments/<int:pk>/update/', comment_views.comment_update, name='comment-update'),
    path('comments/<int:pk>/delete/', comment_views.comment_delete, name='comment-delete'),

    # Reply URLs
    path('reply/', reply_views.reply_list, name='reply-list'),
    path('reply/create/', reply_views.reply_create, name='reply-create'),
    path('reply/<int:pk>/', reply_views.reply_detail, name='reply-detail'),
    path('reply/<int:pk>/update/', reply_views.reply_update, name='reply-update'),
    path('reply/<int:pk>/delete/', reply_views.reply_delete, name='reply-delete'),
]
