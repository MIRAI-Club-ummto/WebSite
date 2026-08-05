from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import LoginSerializer, UserSerializer


class LoginView(APIView):
    """POST /api/accounts/login/  -> connecte l'admin et crée une session"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if user is None:
            return Response({"detail": "Identifiant ou mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_staff:
            return Response({"detail": "Accès réservé aux administrateurs."}, status=status.HTTP_403_FORBIDDEN)

        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutView(APIView):
    """POST /api/accounts/logout/  -> déconnecte l'utilisateur"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Déconnecté."})


class MeView(APIView):
    """GET /api/accounts/me/  -> infos de l'utilisateur connecté"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
