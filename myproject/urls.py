"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("login/",views.UserLoginAPIView.as_view(), name="login" ),
    path("movielist/",views.Movielist.as_view(), name="movies-list"),
    path("watchlist/",views.Watchlist.as_view(), name="movies-list"),
    path("addingwatchlist/",views.addingwatchlist.as_view(), name="addingwatch"),
    path('api/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/register/',views.RegisterAPIView.as_view(),name= 'register'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
