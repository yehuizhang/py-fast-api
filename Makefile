# Define variables
DOCKER_COMPOSE_FILE = docker-compose.yml

# Use Docker Compose to start the service
up:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d

# Use Docker Compose to stop the service
down:
	docker compose -f $(DOCKER_COMPOSE_FILE) down

.PHONY: up down