from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import contact


class ContactView(APIView):

    def post(self, request):

        nom = request.data.get("nom")
        email = request.data.get("email")
        message = request.data.get("message")

        contact.objects.create(
            nom=nom,
            email=email,
            message=message
        )

        return Response(
            {
                "message": "Message envoyé avec succès"
            },
            status=status.HTTP_201_CREATED
        )


    def get(self, request):

        messages = contact.objects.all()

        data = []

        for msg in messages:
            data.append({
                "id": msg.id,
                "nom": msg.nom,
                "email": msg.email,
                "message": msg.message
            })

        return Response(data, status=status.HTTP_200_OK)


    def delete(self, request, id):

        try:
            message = contact.objects.get(id=id)
            message.delete()

            return Response(
                {
                    "message": "Message supprimé avec succès"
                },
                status=status.HTTP_200_OK
            )

        except contact.DoesNotExist:

            return Response(
                {
                    "error": "Message introuvable"
                },
                status=status.HTTP_404_NOT_FOUND
            )