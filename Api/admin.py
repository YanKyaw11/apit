from django.contrib import admin
from .models import Category,Video,VideoComment,Reply

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(VideoComment)
admin.site.register(Reply)