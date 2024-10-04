from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])],blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class VideoComment(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        User = get_user_model()
        return f"Comment by {self.user.email} on {self.video.name}"

class Reply(models.Model):
    comment = models.ForeignKey('VideoComment', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

    @property
    def is_reply(self):
        return self.parent is not None