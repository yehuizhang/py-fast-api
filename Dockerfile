FROM rabbitmq:3-management
LABEL authors="yehuizhang"

# Expose default RabbitMQ port and management console port
EXPOSE 5672 15672

# (Optional) Define environment variables for default user credentials
#ENV RABBITMQ_DEFAULT_USER=user
#ENV RABBITMQ_DEFAULT_PASS=password

# (Optional) Define a default virtual host
#ENV RABBITMQ_DEFAULT_VHOST

# Start RabbitMQ server
CMD ["rabbitmq-server"]