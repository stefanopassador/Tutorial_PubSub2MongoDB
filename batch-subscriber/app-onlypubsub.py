import os
import time
import random
import json
from google.cloud import pubsub_v1

## GCP config
PROJECT_ID = 'streaming-ingestion-382015'
TOPIC_ID = 'sample-topic'
SUBSCRIPTION_ID = 'sample-topic-sub'
SERVICE_ACCOUNT_PATH = './batch-subscription-service-account.json'

subscription_name = f'projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}'

def callback(message):
    print(message.data)
    message.ack()

if __name__ == '__main__':
    with pubsub_v1.SubscriberClient.from_service_account_json(SERVICE_ACCOUNT_PATH) as subscriber: 
        future = subscriber.subscribe(subscription_name, callback)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()
