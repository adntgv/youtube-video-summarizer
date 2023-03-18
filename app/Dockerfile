FROM python:3.9-slim-buster

RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]