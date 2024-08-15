import json
import pika


def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Received message: {}".format(message))

    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

queue = channel.queue_declare("myqueue_messages", durable=True)
queue_name = queue.method.queue
channel.queue_bind(exchange="myqueue", queue=queue_name, routing_key="myqueue.messages")

channel.basic_consume(queue_name, callback)
print("Waiting for new messages...")

channel.start_consuming()
