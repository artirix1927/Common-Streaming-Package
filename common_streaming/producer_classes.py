import redis
from .interfaces import MessageProducer
from kafka import KafkaProducer


class KafkaProducerClass(MessageProducer):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka:9092')

    def produce(self, topic: str, message: str):
        self.producer.send(topic, value=message.encode())


class RedisProducerClass(MessageProducer):
    def __init__(self):
        self.client = redis.Redis.from_url(
            "redis://redis-server:6379/1", decode_responses=True)

    def produce(self, topic: str, message: str):
        self.client.publish(topic, message)
