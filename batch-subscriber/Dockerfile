FROM python:latest
WORKDIR /code
ADD batch-subscription-service-account.json batch-subscription-service-account.json
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "-u", "app.py"]