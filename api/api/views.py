from django.contrib.auth.models import User
from ..models import CustomUser, Company
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(['GET']) 
#@permission_classes([IsAuthenticated])
def get_tokens_for_user(user):
    token = super().get_token(user)
    token['username'] = user.username
    #refresh = RefreshToken.for_user(user)
    #data = {
    #    'refresh': str(refresh),
    #    'access': str(refresh.access_token),
    #}
    return JsonResponse(token)

@api_view(['GET']) 
def getRoutes(request): 
    routes = [ 
        '/api/token',
        '/api/token/refresh/',
        '/api/ApiUserRegister/',
    ]
    return Response(routes)

@api_view(['GET'])
def ApiUserRegister(request, company, username):
    if Company.objects.filter(company=company).exists():
        company_id = Company.objects.get(company=company)
        if User.objects.filter(username=username).exists():
            if CustomUser.objects.filter(company_id=company_id, usernames_id=usernames_id).exists():
                response = dict(company=company, username=username, message="The user is registered in the company", status=status.HTTP_302_FOUND, token=token)
            else:
                response = dict(company=company, username=username, message="The user is not registered in the company", status=status.HTTP_404_NOT_FOUND)
        else:
            response = dict(company=company, username=username, message="The user is not registered", status=status.HTTP_404_NOT_FOUND)
    else:
        response = dict(company=company, username=username, message="The company is not registered", status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(response) 

