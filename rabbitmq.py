import pika

from config import RABBITMQ_DEFAULT_PASS, RABBITMQ_DEFAULT_USER, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_DEFAULT_VHOST


def get_rabbitmq_connection():
    try:
        print(RABBITMQ_DEFAULT_USER)
        credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)
        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            virtual_host=RABBITMQ_DEFAULT_VHOST,
            credentials=credentials,
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        print("RabbitMQ connection initialized successfully")
        return connection, channel
    except Exception as e:
        print(f"Error initializing RabbitMQ connection: {e}")
        return None, None
