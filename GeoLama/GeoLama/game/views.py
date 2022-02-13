from django.shortcuts import render
import random
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderers import PanoJSONRenderer
from .serializer import getCoordsSerializer, setCoordsSerializer
from .models import PanoCoordinates
import sys
sys.path.append('..')
from authentication.serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)


class setCoordsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (PanoJSONRenderer,)
    serializer_class = UserSerializer
    pano_serializer_class = setCoordsSerializer

    def post(self, request):
        serializer = self.serializer_class(request.user)

        coords = request.data.get('panoCoordinates', [{}])
        for data in coords:
            print(1, data)
            serializer = self.pano_serializer_class(data=data)
            print(2, serializer)
            serializer.is_valid(raise_exception=True)
            print(3, serializer)
            serializer.save()

        response = {
            'status': 'created'
        }

        return Response(response, status=status.HTTP_201_CREATED)


class getCoordsAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (PanoJSONRenderer,)
    serializer_class = UserSerializer
    pano_serializer_class = getCoordsSerializer

    def retrieve(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)
        random.seed()
        random_index = random.randint(1, PanoCoordinates.objects.all().count())
        pano_serializer = self.pano_serializer_class(PanoCoordinates.objects.get(coords_id=random_index))
        data = {**serializer.data, **pano_serializer.data}

        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)



