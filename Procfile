release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: heroku config:set DISABLE_COLLECTSTATIC=1
release: curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
web: gunicorn androidproject.wsgi
