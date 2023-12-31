from rest_framework.views import APIView
from .models import Customer
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout


class Customers(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCustomersSerializer
        if self.action == 'retrieve':
            return ListCustomersSerializer
        if self.action == 'update':
            return UpdateCustomerSerializer
        return CustomersSerializer

class LoginView(APIView):
    serializer_class = LoginCustomersSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response("Вы успешно вошли на сайт", status=status.HTTP_200_OK)
            else:
                return Response("Активируйте почту", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("Пользователя не существует", status=status.HTTP_200_OK)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class Courses(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]