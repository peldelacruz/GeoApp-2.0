from django.contrib.auth.models import User
from ..models import CustomUser, Company
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt

class TokenValidate(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {"content": "This view is protected"}
        return Response(content)

@api_view(['GET'])  
def getRoutes(request): 
    routes = [ 
        '/api/token',
        '/api/token/refresh/',
    ]
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, ])
def authenticate_user(request, token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return Response(decoded)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ApiUserRegister(request, company, username):
    if Company.objects.filter(company=company).exists():
        try:
            company_id = Company.objects.get(company=company)
        except:
            response = dict(company=company, username=username, message="The company is not registered", status=status.HTTP_404_NOT_FOUND, token=0)
        else:
            if User.objects.filter(username=username).exists():
                try:
                    usernames_id = User.objects.get(username=username)
                except:
                    response = dict(company=company, username=username, message="The user is not registered in the company", status=status.HTTP_404_NOT_FOUND, token=0)
                else:
                    if CustomUser.objects.filter(company_id=company_id, usernames_id=usernames_id).exists():
                        try:
                            response = dict(company=company, username=username, message="The user is registered in the company", status=status.HTTP_302_FOUND, token=1)
                        except:
                            response = dict(company=company, username=username, message="The user is not registered in the company", status=status.HTTP_404_NOT_FOUND, token=0)
        finally:
            return JsonResponse(response) 

