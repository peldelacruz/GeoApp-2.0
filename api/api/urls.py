#from collections import UserString
from django.urls import path
from . import views
#from api.api.core import views
from api.api.views import  ApiUserRegister, HelloView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.getRoutes),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('ApiUserRegister/', ApiUserRegister, name='ApiUserRegister'),
 ]
