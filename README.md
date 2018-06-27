# Bleuenoix
L'omelette du Benoit

# Introduction
Bleuenoix is a website made to share godtier memes with users.

# Prerequisites

This project is based on Django 2.0.6 and on Pillow.

# Run Server

To generate the virtual environment of the server, simply use the command :

```  virtualenv --no-site-packages --distribute env && source env/bin/activate && pip install -r requirements.txt && deactivate ```

Then do the migrations

```  python3 manage.py makemigrations && python3 manage.py makemigrations benointerest && python3 manage.py migrate ```

For administration purposes, you can create a super user simply by typing and by filling the form

``` python manage.py createsuperuser ```

The website administration is then accessible in ``` /admin ```

Then to run the server

```  source env/bin/activate && python3 manage.py runserver ```

To exit simply press Ctrl-C and type ``` deactivate```