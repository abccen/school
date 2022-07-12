from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import views, response, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from auth_app.serializers import RegisterSerializers
from auth_app.serializers import UserSerializer


class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        if not User.objects.filter(username=login).exists():
            return Response(f'{login} - does not exists')
        user = User.objects.get(username=login)
        password = request.data.get('password')
        pass_check = check_password(password, user.password)
        if not pass_check:
            return Response('password incorrect')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})





class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})

