CURRENT_DIR := $(shell pwd)
DOCKER_NAME ?= avd-quickstart
USERNAME := avd
USER_UID ?= $(shell id -u)
USER_GID ?= $(shell id -g)
PLATFORM ?= $(shell uname) 

DOCKER_IMAGE_PRESENT := $(shell docker image ls | grep '^$(DOCKER_NAME)[[:space:]]*latest')

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build docker image
	if [ -z "${DOCKER_IMAGE_PRESENT}" ]; then \
		docker build --rm --pull --no-cache -t avd-quickstart-temp-image -f $(CURRENT_DIR)/.devcontainer/Dockerfile . ; \
		docker build -f $(CURRENT_DIR)/.devcontainer/updateUID.Dockerfile -t $(DOCKER_NAME):latest --build-arg BASE_IMAGE=avd-quickstart-temp-image --build-arg REMOTE_USER=$(USERNAME) --build-arg NEW_UID=$(USER_UID) --build-arg NEW_GID=$(USER_GID) --build-arg IMAGE_USER=$(USERNAME) . ; \
	fi

.PHONY: run
run: build ## run docker image, if the image is not present - build it first
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		echo "There is no need to run another AVD quickstart container inside AVD quickstart container." ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w /home/$(USERNAME)/projects \
			-v $(CURRENT_DIR):/home/$(USERNAME)/projects \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest || true ; \
	fi
