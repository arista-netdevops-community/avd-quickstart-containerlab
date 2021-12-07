CURRENT_DIR = $(shell pwd)
DOCKER_NAME ?= avd-quickstart
AVD_REPOSITORY_NAME ?= avd_lab

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build docker image
	docker build --rm --pull -t $(DOCKER_NAME):latest -f $(CURRENT_DIR)/.devcontainer/Dockerfile .

.PHONY: clab_deploy
clab_deploy: ## Deploy ceos lab
	cd $(AVD_REPOSITORY_NAME)/clab; sudo containerlab deploy --topo $(AVD_REPOSITORY_NAME).clab.yml

.PHONY: clab_destroy
clab_destroy: ## Destroy ceos lab
	cd $(AVD_REPOSITORY_NAME)/clab; sudo containerlab destroy --topo $(AVD_REPOSITORY_NAME).clab.yml --cleanup

.PHONY: clab_graph
clab_graph: ## Build lab graph
	cd $(AVD_REPOSITORY_NAME)/clab; sudo containerlab graph --topo $(AVD_REPOSITORY_NAME).clab.yml

.PHONY: rm
rm: ## Remove all containerlab directories
	sudo rm -rf $(AVD_REPOSITORY_NAME); sudo rm .cookiecutters/cookiecutter.json

.PHONY: run
run: ## run docker image. This requires cLab "custom_mgmt" to be present
	-docker run --network custom_mgmt --rm -it -v $(CURRENT_DIR)/:/home/avd/projects \
	    -e AVD_GIT_USER="$(shell git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
	    -v /etc/hosts:/etc/hosts $(DOCKER_NAME):latest || true

.PHONY: onboard
onboard: ## onboard devices to CVP
	python3 $(CURRENT_DIR)/$(AVD_REPOSITORY_NAME)/onboard_devices_to_cvp.py

.PHONY: inventory_evpn_aa
inventory_evpn_aa: ## onboard devices to CVP
	docker run --rm -it -v $(CURRENT_DIR)/:/home/avd/projects \
	    -e AVD_GIT_USER="$(shell git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
	    -v /etc/hosts:/etc/hosts $(DOCKER_NAME):latest /home/avd/projects/cook_and_cut.py --input_directory CSVs_EVPN_AA

.PHONY: inventory_evpn_mlag
inventory_evpn_mlag: ## onboard devices to CVP
	docker run --rm -it -v $(CURRENT_DIR)/:/home/avd/projects \
	    -e AVD_GIT_USER="$(shell git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
	    -v /etc/hosts:/etc/hosts $(DOCKER_NAME):latest /home/avd/projects/cook_and_cut.py --input_directory CSVs_EVPN_MLAG

.PHONY: avd_build_eapi
avd_build_eapi: ## build configs and configure switches via eAPI
	cd $(CURRENT_DIR)/$(AVD_REPOSITORY_NAME); ansible-playbook playbooks/fabric-deploy-eapi.yml

.PHONY: avd_build_cvp
avd_build_cvp: ## build configs and configure switches via eAPI
	cd $(CURRENT_DIR)/$(AVD_REPOSITORY_NAME); ansible-playbook playbooks/fabric-deploy-cvp.yml
