CURRENT_DIR := $(shell pwd)
DOCKER_NAME ?= avd-quickstart
USERNAME := avd
USER_UID ?= $(shell id -u)
USER_GID ?= $(shell id -g)

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build docker image
	docker build --rm --pull --no-cache -t avd-quickstart-temp-image -f $(CURRENT_DIR)/.devcontainer/Dockerfile .
	docker build -f $(CURRENT_DIR)/.devcontainer/updateUID.Dockerfile -t $(DOCKER_NAME):latest --build-arg BASE_IMAGE=avd-quickstart-temp-image --build-arg REMOTE_USER=$(USERNAME) --build-arg NEW_UID=$(USER_UID) --build-arg NEW_GID=$(USER_GID) --build-arg IMAGE_USER=$(USERNAME) .
