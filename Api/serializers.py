from rest_framework import serializers
from .models import Video, Category, VideoComment,Reply

class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %I:%M %p', read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %I:%M %p', read_only=True)
    
    class Meta:
        model = Video
        fields = '__all__'

class VideoCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoComment
        fields = ['id', 'user', 'text', 'created_at', 'video','updated_at']

class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = ['id', 'user', 'text', 'created_at', 'parent', 'comment','replies']
