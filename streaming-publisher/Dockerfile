FROM python:latest
WORKDIR /code
ADD streaming-ingestion-service-account.json streaming-ingestion-service-account.json
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "-u", "app.py"]