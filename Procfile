release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: heroku config:set DISABLE_COLLECTSTATIC=1
release: sudo snap install --classic heroku

web: gunicorn androidproject.wsgi
