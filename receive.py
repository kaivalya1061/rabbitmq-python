import pika
import json

#connecting to channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
 
#creating queue hello
channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))

#To consume messages present in queue
channel.basic_consume(callback,
                      queue='test',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
