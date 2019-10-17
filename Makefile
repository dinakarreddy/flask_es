COMPOSE=docker-compose -f ./docker-compose.yml
VOLUMES_DIR=volumes
FLASK_IMAGE_TAG=flask_es
FLASK_DOCKERFILE=Dockerfile
FLASK_IMAGE_BUILD_CONTEXT=./


build: check-pre-requisites
	docker build -t $(FLASK_IMAGE_TAG) -f $(FLASK_DOCKERFILE) $(FLASK_IMAGE_BUILD_CONTEXT)

up: check-pre-requisites build
	$(COMPOSE) up -d

down: check-pre-requisites
	$(COMPOSE) down
	#rm -rf $(VOLUMES_DIR) # remove this line for data persistence between restarts

check-pre-requisites:
	@command -v docker || (echo "Docker not installed!" && exit 1)
	@command -v docker-compose || (echo "Docker compose not installed!" && exit 1)

check-eb-installed:
	@eb --version || (echo "eb not installed" && exit 1)
