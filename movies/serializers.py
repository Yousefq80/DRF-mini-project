from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import Movies,Watchlist


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","username", "password","first_name","last_name","email"]

    # def create(self, validated_data):
        
    #     username = validated_data["username"]
    #     password = validated_data["password"]
    #     first_name = validated_data["first_name"]
    #     last_name = validated_data["last_name"]
    #     email = validated_data["email"]
        
    #     new_user = User(username=username)
    #     new_user.set_password(password)
    #     new_user.save()
    #     return new_user
    
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     token, created = Token.get_or_create(user_id=response.data["id"])
    #     response.data["token"] = str(token)
    #     return response


User = get_user_model()

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     token = serializers.CharField(read_only=True, allow_blank = True)
#     def validate(self, data):
#         my_username = data.get("username")
#         my_password = data.get("password")

#         try:
#             user_obj = User.objects.get(username=my_username)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("This username does not exist")

#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination!")

#         payload = RefreshToken.for_user(user_obj)
#         token = str(payload.access_token)

#         data["token"] = token
#         return data
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['name'] = user.username
        token['email'] = user.email
        # ...

        return token
class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ["user","movie","watched"]

class MoviesSerializer(serializers.ModelSerializer):
    movielist = WatchlistSerializer(many=True)
    class Meta:
        model = Movies
        fields = ["movie"]



class UpdatewatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ["movie", "watched"]
