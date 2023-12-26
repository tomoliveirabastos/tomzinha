import pika
from credenciais import credenciais

c = credenciais()
username = c['rabbitmq_username']
senha = c['rabbitmq_senha']
host = c['rabbitmq_host']

def send_message(message):
       credentials = pika.PlainCredentials(username, senha)
       parameters = pika.ConnectionParameters(host, 5672, "/", credentials)
       queue_name = 'tomzinha'
       connection = pika.BlockingConnection(parameters)
       channel = connection.channel()
       channel.queue_declare(queue='tomzinha')
       channel.basic_publish(exchange='', routing_key=queue_name, body=message)