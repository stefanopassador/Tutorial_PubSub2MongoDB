import os
import time
import random
import json
from google.cloud import pubsub_v1
from pymongo import MongoClient

## GCP config
PROJECT_ID = 'streaming-ingestion-382015'
SERVICE_ACCOUNT_PATH = './batch-subscription-service-account.json'
TOPIC_ID = 'sample-topic'
SUBSCRIPTION_ID = 'sample-topic-sub'

topic_name = f'projects/{PROJECT_ID}/topics/{TOPIC_ID}'
subscription_name = f'projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}'

## MongoDB config
client = MongoClient('mongodb://user:pass@mongodb')
db = client['sample-database']


def callback(message):
    print(message.data)
    messages = db.messages
    messages.insert_one(json.loads(message.data))
    message.ack()

if __name__ == '__main__':
    with pubsub_v1.SubscriberClient.from_service_account_json(SERVICE_ACCOUNT_PATH) as subscriber: 
        future = subscriber.subscribe(subscription_name, callback)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()