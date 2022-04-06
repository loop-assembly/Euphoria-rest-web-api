from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,MenuSerializer,Cov_data_Serializer,cov_name_Serializer
from .models import User,Menu,cov_name,cov_data
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   authentication_classes ={TokenAuthentication,}
   permission_classes =(UpdateOwnProfile,)
   filter_backends = (filters.SearchFilter,)
   search_fields = ('name','email')
   lookup_field = "email"
  
  
   # def update(self,request,pk=None):
   #      '''Handle a particular update of an object'''
   #      if not self.serializer_class.is_valid(raise_exception=False):
   #         return Response({"Fail": "blablal"})
        

   
   

class MenuViewSet(viewsets.ModelViewSet):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer
   filter_backends = (filters.SearchFilter,)
   search_fields = ('name','item_name')

class UserLoginApiView(ObtainAuthToken):
   '''Handle creating user authentication token'''
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class cov_name_ViewSet(viewsets.ModelViewSet):
   queryset = cov_name.objects.all()
   serializer_class = cov_name_Serializer
   # authentication_classes ={TokenAuthentication,}
   # permission_classes =(UpdateOwnProfile,)
   filter_backends = (filters.SearchFilter,)
   search_fields = ('name','number')
   lookup_field = "name"


class cov_data_ViewSet(viewsets.ModelViewSet):
   queryset = cov_data.objects.all()
   serializer_class = Cov_data_Serializer
   # authentication_classes ={TokenAuthentication,}
   # permission_classes =(UpdateOwnProfile,)
   # filter_backends = (filters.SearchFilter,)
   # search_fields = ('name','number')
   # lookup_field = "name"