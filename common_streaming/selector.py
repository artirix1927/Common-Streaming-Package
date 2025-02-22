try:
    from django.conf import settings
    DJANGO_AVAILABLE = True
except ImportError:
    DJANGO_AVAILABLE = False

from .consumer_classes import KafkaConsumerClass, RedisConsumerClass
from .producer_classes import KafkaProducerClass, RedisProducerClass


def get_message_broker():
    broker_type = "kafka"  # Default
    if DJANGO_AVAILABLE:
        broker_type = getattr(settings, "MESSAGE_BROKER", "kafka")
    return broker_type


def get_message_producer():
    broker_type = get_message_broker()
    return KafkaProducerClass() if broker_type == "kafka" else RedisProducerClass()


def get_message_consumer():
    broker_type = get_message_broker()
    return KafkaConsumerClass() if broker_type == "kafka" else RedisConsumerClass()
