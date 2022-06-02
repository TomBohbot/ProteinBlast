FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get update && apt-get install --assume-yes --verbose-versions \
  ncbi-blast+

COPY ./app /code/app

CMD ["python", "app/main.py", "--host", "0.0.0.0", "--port", "5000"]