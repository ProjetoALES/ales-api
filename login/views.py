from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AuthenticatedView(APIView):

    def get(self, request):
        content = {'message': 'Hello, you are authenticated!'}
        return Response(content)
