from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "name", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Class for serializing authentication tokens."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )

        if not user:
            msg = "Unable to authenticate using this credential."
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
