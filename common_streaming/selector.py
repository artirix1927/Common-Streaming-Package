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
        broker_type = getattr(settings, "BROKER_TYPE", "kafka")
        broker_path = getattr(settings, "BROKER_PATH")
    return broker_type, broker_path


def get_message_producer():
    type, path = get_message_broker()
    return KafkaProducerClass(path) if type == "kafka" else RedisProducerClass(path)


def get_message_consumer():
    type, path = get_message_broker()
    return KafkaConsumerClass(path) if type == "kafka" else RedisConsumerClass(path)
