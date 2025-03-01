import redis
from .interfaces import MessageProducer
from kafka import KafkaProducer


class KafkaProducerClass(MessageProducer):
    def __init__(self, path: str):
        self.producer = KafkaProducer(bootstrap_servers=path)

    def produce(self, topic: str, message: str):
        self.producer.send(topic, value=message.encode())


class RedisProducerClass(MessageProducer):
    def __init__(self, path: str):
        self.client = redis.Redis.from_url(
            path, decode_responses=True)

    def produce(self, topic: str, message: str):
        self.client.publish(topic, message)
