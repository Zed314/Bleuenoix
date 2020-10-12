FROM python:latest

ENV PROD True

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN mkdir /code/static

RUN chmod u+x /code/entrypoint.sh
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y netcat
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["/code/entrypoint.sh"]