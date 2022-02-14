from django.shortcuts import render
import json

import random
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderers import PanoJSONRenderer, RatingJSONRenderer
from .serializer import getCoordsSerializer, setCoordsSerializer, getRatingSerializer
from .models import PanoCoordinates, Rating
import sys
sys.path.append('..')
from authentication.serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)


class getRatingAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RatingJSONRenderer,)
    serializer_class = UserSerializer
    rating_serializer_class = getRatingSerializer

    def retrieve(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)
        rating = Rating.objects.all()
        data = {
            'rating_users': []
        }
        print(rating)
        for user in rating:
            print(user)
            rating_serializer = self.rating_serializer_class(user)
            print(rating_serializer)
            temp = {
                rating_serializer.data['username']: rating_serializer.data['points']
            }
            data['rating_users'].append(temp)
            # username = user.get('username', None)
            # points = user.get('points', None)
            # serializer_data = json.dumps({
            #     'username': username,
            #     'points': points
            # })
        print(data)
        data = {**serializer.data, **data}
        print(data)

        return Response(data, status=status.HTTP_200_OK)



class setCoordsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (PanoJSONRenderer,)
    serializer_class = UserSerializer
    pano_serializer_class = setCoordsSerializer

    def post(self, request):
        serializer = self.serializer_class(request.user)

        coords = request.data.get('panoCoordinates', None)
        if coords is None:
            response = {
                'status': 'Nothing to create'
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

        for data in coords:
            serializer = self.pano_serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
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

    # def update(self, request, *args, **kwargs):
    #     serializer_data = request.data.get('user', {})
    #
    #     # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
    #     serializer = self.serializer_class(
    #         request.user, data=serializer_data, partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)



