CURRENT_DIR = $(shell pwd)
DOCKER_NAME ?= avd-quickstart

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: deploy
deploy: ## Deploy ceos lab
	sudo containerlab deploy --topo atd-quickstart.clab.yml --reconfigure

.PHONY: destroy
destroy: ## Destroy ceos lab
	sudo containerlab destroy --topo atd-quickstart.clab.yml

.PHONY: graph
graph: ## Build lab graph
	sudo containerlab graph --topo atd-quickstart.clab.yml

.PHONY: rm
rm: ## Remove all containerlab directories
	sudo rm -rf clab-ATD

.PHONY: build
build: ## Build docker image
	docker build --rm --pull -t $(DOCKER_NAME):latest -f $(CURRENT_DIR)/.devcontainer/Dockerfile .

.PHONY: run
run: ## run docker image
	docker run --network custom_mgmt --rm -it -v $(CURRENT_DIR)/:/home/avd/projects \
	    -e AVD_GIT_USER="$(shell git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
	    -v /etc/hosts:/etc/hosts $(DOCKER_NAME):latest

.PHONY: onboard
onboard: ## onboard devices to CVP
	$(CURRENT_DIR)/onboard_devices_to_cvp.py

.PHONY: inventory
inventory: ## onboard devices to CVP
	$(CURRENT_DIR)/create-avd-repository.py -out .
