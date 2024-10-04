from django.utils.timezone import localtime
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

class CustomUserSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('uuid', 'name', 'usercode', 'created_at', 'email', 'password', 'is_approved', 'is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def get_created_at(self, obj):
        local_time = localtime(obj.created_at)
        return local_time.strftime('%d/%m/%Y %I:%M %p')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            usercode=validated_data['usercode'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
        return value

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

class PasswordResetSerializer(serializers.Serializer):
    uidb64 = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def save(self):
        try:
            uid = force_str(urlsafe_base64_decode(self.validated_data['uidb64']))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            raise serializers.ValidationError("Invalid user.")

        if not default_token_generator.check_token(user, self.validated_data['token']):
            raise serializers.ValidationError("Token is invalid or expired.")

        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
