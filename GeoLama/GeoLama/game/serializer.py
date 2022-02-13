from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import PanoCoordinates


class setCoordsSerializer(serializers.ModelSerializer):
    """ Сериализация сохранения координат. """

    class Meta:
        model = PanoCoordinates
        # Перечислить все поля, которые могут быть включены в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = ['longitude', 'latitude']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        print(data)
        try:
            float(data['longitude'])
            float(data['latitude'])
        except Exception:
            raise serializers.ValidationError("coordinates is not float")
        if data['longitude'] is None or data['latitude'] is None:
            raise serializers.ValidationError("coordinates is not float")
        return data


class getCoordsSerializer(serializers.ModelSerializer):
    """ Сериализация возврата координат. """

    class Meta:
        model = PanoCoordinates
        # Перечислить все поля, которые могут быть включены в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = ['coords_id', 'longitude', 'latitude']
