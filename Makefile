CURRENT_DIR = $(shell pwd)
DOCKER_NAME ?= avd-quickstart

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clab_deploy
clab_deploy: ## Deploy ceos lab
	cd avd_test/clab; sudo containerlab deploy --topo avd_test.clab.yml

.PHONY: clab_destroy
clab_destroy: ## Destroy ceos lab
	cd avd_test/clab; sudo containerlab destroy --topo avd_test.clab.yml --cleanup

.PHONY: clab_graph
clab_graph: ## Build lab graph
	cd avd_test/clab; sudo containerlab graph --topo avd_test.clab.yml

.PHONY: rm
rm: ## Remove all containerlab directories
	sudo rm -rf clab-ATD

.PHONY: build
build: ## Build docker image
	docker build --rm --pull -t $(DOCKER_NAME):latest -f $(CURRENT_DIR)/.devcontainer/Dockerfile .

.PHONY: build_alpine
build_alpine: ## Build docker image
	cd $(CURRENT_DIR)/alpine_host; docker build --rm --pull -t alpine-host .

.PHONY: run
run: ## run docker image
	docker run --network custom_mgmt --rm -it -v $(CURRENT_DIR)/:/home/avd/projects \
	    -e AVD_GIT_USER="$(shell git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
	    -v /etc/hosts:/etc/hosts $(DOCKER_NAME):latest

.PHONY: onboard
onboard: ## onboard devices to CVP
	python3 $(CURRENT_DIR)/avd_test/onboard_devices_to_cvp.py

.PHONY: inventory
inventory: ## onboard devices to CVP
	$(CURRENT_DIR)/cook_and_cut.py

.PHONY: avd_build_eapi
avd_build_eapi: ## build configs and configure switches via eAPI
	cd $(CURRENT_DIR)/avd_test; ansible-playbook playbooks/fabric-deploy-eapi.yml

.PHONY: avd_build_cvp
avd_build_cvp: ## build configs and configure switches via eAPI
	cd $(CURRENT_DIR)/avd_test; ansible-playbook playbooks/fabric-deploy-cvp.yml
