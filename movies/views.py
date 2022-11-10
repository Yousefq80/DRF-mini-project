from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import UpdatewatchlistSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Movies,Watchlist 
from movies import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import filterset
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

class Movieapilist(ListAPIView):
     queryset = Movies.objects.all()
     serializer_class=serializers.MoviesSerializer

class Watchapilist(ListAPIView):
    
     
     def get_serializer_class(self):
        if self.request.user.is_authenticated:
           return serializers.WatchlistSerializer
        return serializers.MoviesSerializer
          
        
     def get_queryset(self):
        if self.request.user.is_authenticated:
           user = self.request.user
           return Watchlist.objects.filter(user=user)
        return Movies.objects.all()
          

        # Keeping the below codes for refrences only 
        # queryset = Watchlist.objects.all()
        # serializer_class =serializers.WatchlistSerializer
        # filterset_class = MoviesFilter
        # queryset = Watchlist.objects()
        # def get_queryset(self):
        #  user = self.request.user
        #  return user.watchlist_set.all()
        # permission_classes = [IsAuthenticated]
        # serializer_class =serializers.WatchlistSerializer
       
        # def get_queryset(self):
        #   queryset = Watchlist.objects.all()
        #   username = self.request.query_params.get('username')
        #   if username is not None:
        #     queryset = queryset.filter(user__username=username)
        #     return queryset
            
        #     return Response(serializer.data)
    # def get_serializer_class(self):
    #     if self.request.user.is_authenticated:
    #        return Watchlist.objects.filter(user=self.request.user)
           
        # return  serializers.MoviesSerializer

class addingwatchlist(CreateAPIView):
     serializer_class = UpdatewatchlistSerializer
     lookup_field = 'id'
     lookup_url_kwarg = 'movie_id'
     def perform_create(self, serializer):
      movie_id =self.kwargs['moive_id']
      serializer.save(user=self.request.user, movie_id=movie_id)