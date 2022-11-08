from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import UpdatewatchlistSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from movies.models import Movies,Watchlist 
from movies import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        return response

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# # class UserLoginAPIView(APIView):
# #     serializer_class = UserLoginSerializer

#     def post(self, request):
#         my_data = request.data
#         serializer = UserLoginSerializer(data=my_data)
#         if serializer.is_valid(raise_exception=True):
#             valid_data = serializer.data
#             return Response(valid_data, status=HTTP_200_OK)
#         else:
#             return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class Movielist(ListAPIView):
     queryset = Movies.objects.all()
    #  serializer_class=serializers.MoviesSerializer

class Watchlist(ListAPIView):
    serializer_class=serializers.WatchlistSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
           return Watchlist.objects.filter(user=self.request.user)
           
        # return  serializers.MoviesSerializer

class addingwatchlist(CreateAPIView):
     serializer_class = UpdatewatchlistSerializer
     lookup_field = 'id'
     lookup_url_kwarg = 'movie_id'
     def perform_create(self, serializer):
      movie_id =self.kwargs['moive_id']
      serializer.save(user=self.request.user, movie_id=movie_id)