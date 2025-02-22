

class MessageProducer:
    def produce(self, topic: str, message: str):
        raise NotImplementedError


class MessageConsumer:
    def consume(self, topic: str, callback):
        raise NotImplementedError
