FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "req.py"]

# docker build . --tag test_requests:0
# docker run test_requests:0