from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'phone_number', 'user_type', 'password'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create and return a new user with a hashed password."""
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password) 
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update and return an existing user, hashing the password if provided."""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
