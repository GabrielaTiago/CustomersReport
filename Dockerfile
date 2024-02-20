FROM python:3.8

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

CMD ["python", "./src/main.py"]