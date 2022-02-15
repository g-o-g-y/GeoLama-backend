web: gunicorn GeoLama.GeoLama.GeoLama.wsgi
worker: python GeoLama.GeoLama.manage.py makemigrations
worker: python GeoLama.GeoLama.manage.py migrate
worker: python GeoLama.GeoLama.manage.py runserver