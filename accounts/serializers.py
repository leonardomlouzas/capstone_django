from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.exceptions import UniqueException
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'user_uuid',
            'first_name',
            'last_name',
            'password',
            'email',
            'created_at',
            'is_staff',
            'is_superuser',
        )

        extra_kwargs = {'password': {'write_only': True}}

        read_only_fields = ('is_staff', 'is_superuser')

    def validate_first_name(self, first_name: str):
        return first_name.title()

    def validate_last_name(self, last_name: str):
        return last_name.title()

    def validate_email(self, email: str):
        email_exists = Account.objects.filter(email=email.lower()).exists()

        if email_exists:
            raise UniqueException({'detail': 'email already exists'})

        return email

    def create(self, validated_data: dict):
        return Account.objects.create_user(**validated_data)


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'user_uuid',
            'first_name',
            'last_name',
            'password',
            'email',
            'created_at',
            'is_staff',
            'is_superuser',
        )

        extra_kwargs = {'password': {'write_only': True}}

    def validate_first_name(self, first_name: str):
        return first_name.title()

    def validate_last_name(self, last_name: str):
        return last_name.title()

    def validate_email(self, email: str):
        return email.lower()

    def update(self, instance: Account, validated_data: dict):
        user: Account = self.context['request'].user

        is_staff = validated_data.pop('is_staff', False)
        is_superuser = validated_data.pop('is_superuser', False)

        if user.is_superuser:
            validated_data.setdefault('is_staff', is_staff)
            validated_data.setdefault('is_superuser', is_superuser)

        for key, value in validated_data.items():
            if key is 'password':
                value = make_password(value)

            setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
