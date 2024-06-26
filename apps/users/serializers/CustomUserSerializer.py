from rest_framework import serializers
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, data):
        user = CustomUser.objects._create_user(
            data['email'],
            data['password'],
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        if validated_data.get('password') is not None:
            instance.set_password(validated_data.get('password'))
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.is_staff = validated_data.get('is_staff',instance.is_staff)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.date_joined = validated_data.get('date_joined',instance.date_joined)
        instance.photo = validated_data.get('photo',instance.photo)
        instance.save()
        return instance