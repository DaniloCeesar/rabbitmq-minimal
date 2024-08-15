import json
import pika
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["POST"])
def publisher():
    message = request.get_json()

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672)
    )
    channel = connection.channel()
    channel.exchange_declare(exchange="myqueue", exchange_type="direct", durable=True)

    channel.basic_publish(
        exchange="myqueue", routing_key="myqueue.messages", body=json.dumps(message)
    )

    connection.close()

    print("Message sent to the queue")
    return jsonify(success=True), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
