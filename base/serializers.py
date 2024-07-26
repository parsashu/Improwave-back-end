from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email','password', 'name', 'bio', 'profile_pic', 'token')

    def get_token(self, obj):
        # Retrieve or create a token for the user
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
