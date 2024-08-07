import pika, sys, os

from rabbitmq import get_rabbitmq_connection


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    connection, channel = get_rabbitmq_connection()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
