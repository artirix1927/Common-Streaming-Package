from typing import Callable
import redis
from .interfaces import MessageConsumer
from kafka import KafkaConsumer


class KafkaConsumerClass(MessageConsumer):
    def __init__(self, path: str):
        self.consumer = KafkaConsumer(bootstrap_servers=path)

    def consume(self, topic: str, callback: Callable):
        self.consumer.subscribe([topic])
        for message in self.consumer:
            callback(message.value)


class RedisConsumerClass(MessageConsumer):
    def __init__(self, path: str):
        self.client = redis.Redis.from_url(
            path, decode_responses=True)

    def consume(self, topic: str, callback: Callable):
        pubsub = self.client.pubsub()
        pubsub.subscribe(topic)
        for message in pubsub.listen():
            if message['type'] == 'message':
                callback(message['data'])
