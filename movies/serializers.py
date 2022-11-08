from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Movies,Watchlist

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password","first_name","last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return new_user


User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, allow_blank = True)
    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["token"] = token
        return data

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ["title"]

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ["movie","watched"]

class UpdatewatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ["movie", "watched"]
