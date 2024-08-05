FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essenatial \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /code

# set permission

RUN chmod +x /code/src

RUN pip install --no-cache-dir --upgrade -r code/src/requirments.txt

EXPOSE 8005

WORKDIR /code/src

ENV PYTHONPATH="${PYTHONPATH:/code/src}"

CMD pip install -e .