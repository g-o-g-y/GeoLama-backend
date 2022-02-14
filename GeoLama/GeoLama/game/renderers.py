import json

from rest_framework.renderers import JSONRenderer


class RatingJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Если представление выдает ошибку (например, пользователь не может
        # быть аутентифицирован), data будет содержать ключ error. Мы хотим,
        # чтобы стандартный JSONRenderer обрабатывал такие ошибки, поэтому
        # такой случай необходимо проверить.
        errors = data.get('errors', None)
        if errors is not None:
            # Позволим стандартному JSONRenderer обрабатывать ошибку.
            return super(RatingJSONRenderer, self).render(data)

        rating_users = data.get('rating_users', None)
        if rating_users is not None:
            del data['rating_users']
        else:
            data = {
                'errors': {
                    "error": ["A user with this email and password was not found."]
                }
            }
            return super(RatingJSONRenderer, self).render(data)

        # Наконец, мы можем отобразить наши данные в пространстве имен 'user'.
        return json.dumps({
            'user': data,
            'rating_users': rating_users
        })



class PanoJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Если представление выдает ошибку (например, пользователь не может
        # быть аутентифицирован), data будет содержать ключ error. Мы хотим,
        # чтобы стандартный JSONRenderer обрабатывал такие ошибки, поэтому
        # такой случай необходимо проверить.
        errors = data.get('errors', None)
        if errors is not None:
            # Позволим стандартному JSONRenderer обрабатывать ошибку.
            return super(PanoJSONRenderer, self).render(data)

        coords_id = data.get('coords_id', None)
        longitude = data.get('longitude', None)
        latitude = data.get('latitude', None)
        if coords_id is not None:
            del data['coords_id']
            del data['longitude']
            del data['latitude']
        else:
            data = {
                'errors': {
                    "error": ["A user with this email and password was not found."]
                }
            }
            return super(PanoJSONRenderer, self).render(data)

        # Наконец, мы можем отобразить наши данные в пространстве имен 'user'.
        return json.dumps({
            'user': data,
            'panoCoordinates': {
                'longitude': longitude,
                'latitude': latitude
            }
        })
