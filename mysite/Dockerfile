FROM python:3.8

COPY . .
RUN . /env/bin/activate && pip install -r requirements.txt

CMD . /env/bin/activate && gunicorn --bind 0.0.0.0:8080 website.wsgi