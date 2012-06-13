#!/usr/bin/python

import pika
import sys


cred=pika.credentials.PlainCredentials(username='guest',password='7d0fe7e2f9c405734dd41d84cb91e877')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='172.16.55.131', credentials=cred))
channel = connection.channel()
channel.queue_delete(queue='notifications.error')
#channel.queue_bind(exchange='nova',
#                       queue='notifications.error',
#                       routing_key='notifications.error')

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

#channel.basic_consume(callback,
#                      queue='',
#                      no_ack=True)

#channel.start_consuming()

