FROM python:3.14.2-slim

WORKDIR /app

RUN apt-get update && apt-get clean && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "api.py"]