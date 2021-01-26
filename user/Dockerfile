FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD gunicorn user.wsgi:application --bind 0.0.0.0:$PORT