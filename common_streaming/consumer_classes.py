from typing import Callable
import redis
from .interfaces import MessageConsumer
from kafka import KafkaConsumer


class KafkaConsumerClass(MessageConsumer):
    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers='kafka:9092')

    def consume(self, topic: str, callback: Callable):
        self.consumer.subscribe([topic])
        for message in self.consumer:
            callback(message.value)


class RedisConsumerClass(MessageConsumer):
    def __init__(self):
        self.client = redis.Redis.from_url(
            "redis://redis-server:6379/1", decode_responses=True)

    def consume(self, topic: str, callback: Callable):
        pubsub = self.client.pubsub()
        pubsub.subscribe(topic)
        for message in pubsub.listen():
            if message['type'] == 'message':
                callback(message['data'])
