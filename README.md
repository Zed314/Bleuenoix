# Bleuenoix
L'omelette du Benoit

# Introduction
Bleuenoix is a website made to share godtier memes with users.

# Prerequisites

This project is based on Django 2.0.6 and on Pillow. Thus, it requires Python3 and pip3 (python3-pip).

# Install and Run Server

## Using virtualenv

To generate the virtual environment of the server, simply use the command :

```  virtualenv --no-site-packages --distribute env && source env/bin/activate && pip install -r requirements.txt ```

Then do the migrations

```  python3 manage.py makemigrations && python3 manage.py makemigrations bleuenoix && python3 manage.py migrate ```

For administration purposes, you can create a super user simply by typing and by filling the form

``` python manage.py createsuperuser ```

The website administration is then accessible in ``` /admin ```

Then to run the server

```  source env/bin/activate && python3 manage.py runserver ```

To exit simply press Ctrl-C and type ``` deactivate```

## Using docker-compose

Just type

```docker-compose up```

:)

# Addtional installation

I recommand the usage of pylint-django to write code. To install it, simply run the command:

``` pip install pylint-django ```

And if you use VSCode, add this to your seetings:

```"python.linting.pylintArgs": ["--load-plugins=pylint_django"],```