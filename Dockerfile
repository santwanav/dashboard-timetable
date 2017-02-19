FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

ARG port=60002
ENV TIME_TABLE_HTTP_PORT=$port
EXPOSE $port

ENTRYPOINT ["/app/server.py"]
