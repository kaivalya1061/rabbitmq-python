import pika
import json

#connecting to channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
 
#creating queue hello
channel.queue_declare(queue='hello')

#sending message to queue
#a default exchange identified by an empty string
message = {'email':'xujxTVmX6105RtSiZBAzhnAn4iJabqaEysSDNRnI6YoMR0pel6/3hod94fL0E1xm','client':1,'remove_client':False,'domain':'2'}
message = {'email':'k@g','name':'kg'}

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(message))
print(" [x] Sent 'Hello World!'")

#close the connection
connection.close()

