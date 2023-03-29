FROM python:latest
WORKDIR /code
ADD streaming-publisher-service-account.json streaming-publisher-service-account.json
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "-u", "app.py"]