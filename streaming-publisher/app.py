import os
import time
import random
import json
from google.cloud import pubsub_v1

PROJECT_ID = 'streaming-ingestion-382015'
SERVICE_ACCOUNT_PATH = './streaming-publisher-service-account.json'
TOPIC_ID = 'sample-topic'

def publish_message(message):
    publisher = pubsub_v1.PublisherClient.from_service_account_json(SERVICE_ACCOUNT_PATH)
    topic_name = f'projects/{PROJECT_ID}/topics/{TOPIC_ID}'
    future = publisher.publish(topic_name, json.dumps(message).encode('utf-8'))
    future.result()


def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    message = {
        'key': n,
        'value': random.randint(1,100000)
    }
    publish_message(message)

if __name__ == '__main__':
    print('Application started')
    
    n = 0
    while True:
        add_new_row(n)
        n = n + 1
        print(f'Published message: {n}')
        time.sleep(1)
