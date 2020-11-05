from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from . import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloViewSerializer

    def get(self, request, format=None):
        context = ['Hello']
        return Response({'message': context})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Update full object
        return Response({'message': 'Put'})

    def patch(self, request, pk=None):
        # Update part of object
        return Response({'message': 'Patch'})

    def delete(self, request, pk=None):

        return Response({'message': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloViewSerializer

    def list(self, request):
        return Response({'message': 'Hello'})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'message': 'get'})

    def update(self, request, pk=None):
        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'message': 'DELETE'})
