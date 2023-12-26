import pika
import json
import gpt_response
import pyttsx3
from credenciais import credenciais

c = credenciais()
username = c['rabbitmq_username']
senha = c['rabbitmq_senha']
host = c['rabbitmq_host']

credentials = pika.PlainCredentials(username, senha)
parameters = pika.ConnectionParameters(host, 5672, "/", credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='tomzinha')
engine = pyttsx3.init()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
    j = json.loads(body)
    
    t = ""
    
    if j["gpt"] == "SIM":
        t = gpt_response.make_question(body)

    else:
        t = j["message"]

    engine.say(t)
    engine.runAndWait()
    
    
channel.basic_consume(on_message_callback=callback, queue='tomzinha', auto_ack=True)
channel.start_consuming()