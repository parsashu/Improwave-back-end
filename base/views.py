from .models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status



@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users_profile = User.objects.all()
        serializer = UserSerializer(users_profile, many=True)
        return Response(serializer.data)
 

@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)




