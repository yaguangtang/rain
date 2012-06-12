import pika
import sys


cred=pika.credentials.PlainCredentials(username='guest',password='beyond630')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials=cred))
channel = connection.channel()
channel.queue_bind(exchange='nova',
                       queue='notifications.error',
                       routing_key='*')

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue='notifications.error',
                      no_ack=True)

channel.start_consuming()

