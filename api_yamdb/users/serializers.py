from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.Serializer):
    """Сериализатор для создания User-a"""
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    email = serializers.EmailField(
        max_length=254,
        required=True
    )

    def validate(self, data):
        if_username = User.objects.filter(username=data['username']).exists()
        if_email = User.objects.filter(email=data['email']).exists()
        if data['username'].lower() == 'me':
            raise serializers.ValidationError(
                'Использовать имя me запрещено!'
            )
        if User.objects.filter(username=data['username'],
                               email=data['email']).exists():
            return data
        if if_username:
            raise serializers.ValidationError('Данные уже были использованы')
        if if_email:
            raise serializers.ValidationError('Почта уже была использована')
        return data


class UserRecieveJWTSerializer(serializers.Serializer):
    """Сериализатор для получения токена JWT."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, username):
        if username.lower() == 'me':
            raise serializers.ValidationError(
                'Использовать имя me запрещено!'
            )
        return username
