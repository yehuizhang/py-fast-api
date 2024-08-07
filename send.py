from datetime import datetime

import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials, virtual_host='chaos'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} bye')

print("Sent a message")
connection.close()