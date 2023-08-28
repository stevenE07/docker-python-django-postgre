# django imports
from django.contrib.auth import login

# rest_framework imports
from rest_framework import generics, permissions, views, response
from rest_framework.authtoken.serializers import AuthTokenSerializer

# knox imports
from knox.views import LoginView as KnoxLoginView

# local apps import
from .serializers import PersonaViewSerializer, PersonaSerializer, AuthSerializer
from .models import Persona

class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = PersonaSerializer
    permission_classes = (permissions.AllowAny,)

class ListUserView(generics.ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (permissions.AllowAny,)

class UpdateUserView(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'username'

class DeleteUserView(generics.DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'username'
    
class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = PersonaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
