web: gunicorn djangoWebsite.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py makemigrations VRCpubs
release: python manage.py migrate VRCpubs
