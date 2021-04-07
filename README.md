# Django_Website_publications
A simple website using Django backend and bootstrap frontend to display publications of professors of an university.

### Note: - Refer The docs folder for further info about the project (includes images and demo video)

### Hosted Site: https://cmpn-publications-official.herokuapp.com/

### Demo Video: https://tinyurl.com/y9ltof5p

## To run locally: -
open djangoWebsite/settings.py

In this file:

1) Comment line 14 ( `import django_heroku` ) and line 131 ( `django_heroku.settings(locals())` )

2) Open cmd ( while being on a path where manage.py is directly visible)

3) Run `python manage.py createsuperuser`

4) Run `python manage.py migrate`

5) Run `python manage.py makemigrations`

6) Run `python manage.py runserver`

7) Open the link given by the output

8) To access admin page add `/admin` after the current url


## To run on heroku: -
uncomment lines 14 and 131

1) Create new app from heroku dashboard (first pip install heroku in cmd)

2) Follow steps to upload the files given there in the deploy tab.

3) Then go to resources tab and on any off dynos there.

4) Run `heroku run python3 manage.py createsuperuser

5) Run `heroku run python3 manage.py migrate`

6) Run `heroku run python3 manage.py makemigrations`

7) To access admin page add `/admin` after the current url



