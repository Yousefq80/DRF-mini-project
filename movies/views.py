from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import UserLoginSerializer,UpdatewatchlistSerializer
from movies.models import Movies,Watchlist 
from movies import serializers
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class Watchlist(ListAPIView):
    queryset = Movies.objects.all()
    
    def get_movies(self):
        if self.request.user.is_authenticated:
           return Watchlist.objects.filter(user=self.request.user)
       
        return  serializers.MoviesSerializer

class addingwatchlist(CreateAPIView):
     serializer_class = UpdatewatchlistSerializer
     lookup_field = 'id'
     lookup_url_kwarg = 'movie_id'
     def perform_create(self, serializer):
      movie_id =self.kwargs['moive_id']
      serializer.save(user=self.request.user, movie_id=movie_id)