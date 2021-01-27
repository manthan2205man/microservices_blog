# amqps://ziborigv:EGUW7o28G5N_Jj80_6cIYrAjyb8ucDwV@lionfish.rmq.cloudamqp.com/ziborigv

import pika
import json

class BlogAppProducer(object):
    def __init__(self):
        self.params=pika.URLParameters('amqps://ysyrfqhq:JioBjnZXG0l-9PCDz3PZIsWuBhX-aVFb@lionfish.rmq.cloudamqp.com/ysyrfqhq')
        self.connection = pika.BlockingConnection(self.params)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = json.loads(body) 

    def call(self, method, body):
        self.response = None
        self.corr_id = str(method)
        self.channel.basic_publish(
            exchange='',
            routing_key='user',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        while self.response is None:
            self.connection.process_data_events()
        return self.response
