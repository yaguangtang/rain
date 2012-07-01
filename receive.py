#!/usr/bin/python

import pika
import sys


cred=pika.credentials.PlainCredentials(username='guest',password='password')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1', credentials=cred))
channel = connection.channel()
channel.queue_delete(queue='notifications.info')
#channel.queue_bind(exchange='nova',
#                       queue='notifications.error',
#                       routing_key='notifications.error')

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

#channel.basic_consume(callback,
#                      queue='',
#                      no_ack=True)

#channel.start_consuming()

