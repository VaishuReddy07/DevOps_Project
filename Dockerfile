FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python
COPY . .

EXPOSE 8080

CMD ["python", "runserver.py"]