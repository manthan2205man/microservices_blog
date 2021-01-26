# amqps://ziborigv:EGUW7o28G5N_Jj80_6cIYrAjyb8ucDwV@lionfish.rmq.cloudamqp.com/ziborigv
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

# from blog_user.models import Token, User

params=pika.URLParameters('amqps://ziborigv:EGUW7o28G5N_Jj80_6cIYrAjyb8ucDwV@lionfish.rmq.cloudamqp.com/ziborigv')

connection=pika.BlockingConnection(params)

channel=connection.channel()
channel.queue_declare(queue='blog')

def get_token(email):
    pass
    # user=User.objects.get(email=email)
    # token=Token.objects.get(user=user)
    # token=token.token
    # return token

def on_request(ch, method, props, body):
    email=json.loads(body)
    properties=props.correlation_id
    response = get_token(email)

    ch.basic_publish(exchange='',routing_key=props.reply_to,properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='blog', on_message_callback=on_request, auto_ack=True)
print("BLOG CONSUMER STARTED.")
channel.start_consuming()
channel.close()