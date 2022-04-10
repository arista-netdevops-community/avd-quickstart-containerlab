CURRENT_DIR := $(shell pwd)
DOCKER_NAME ?= avd-quickstart
USERNAME := avd
USER_UID ?= $(shell id -u)
USER_GID ?= $(shell id -g)
PLATFORM ?= $(shell uname)

AVD_REPOSITORY_NAME := avd_lab
CLAB_NAME := ${AVD_REPOSITORY_NAME}

DOCKER_IMAGE_PRESENT := $(shell docker image ls | grep '^$(DOCKER_NAME)[[:space:]]*latest')

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: prepare_macos
prepare_mac_os: ## Prepare Docker Desktop on MacOS for cEOS-based Containerlab
	$(CURRENT_DIR)/MacOS_set_DockerDesktop.sh

.PHONY: build
build: ## Build docker image
	docker build --rm --pull --no-cache -t avd-quickstart-temp-image -f $(CURRENT_DIR)/.devcontainer/Dockerfile . ; \
	docker build -f $(CURRENT_DIR)/.devcontainer/updateUID.Dockerfile -t $(DOCKER_NAME):latest --build-arg BASE_IMAGE=avd-quickstart-temp-image --build-arg REMOTE_USER=$(USERNAME) --build-arg NEW_UID=$(USER_UID) --build-arg NEW_GID=$(USER_GID) --build-arg IMAGE_USER=$(USERNAME) . ; \

.PHONY: run
run: ## run docker image
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		echo "There is no need to run another AVD quickstart container inside AVD quickstart container." ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest || true ; \
	fi

.PHONY: inventory_evpn_aa
inventory_evpn_aa: ## onboard devices to CVP
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		$(CURRENT_DIR)/cook_and_cut.py --input_directory CSVs_EVPN_AA ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest $(CURRENT_DIR)/cook_and_cut.py --input_directory CSVs_EVPN_AA ; \
	fi

.PHONY: inventory_evpn_mlag
inventory_evpn_mlag: ## onboard devices to CVP
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		$(CURRENT_DIR)/cook_and_cut.py --input_directory CSVs_EVPN_MLAG ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest $(CURRENT_DIR)/cook_and_cut.py --input_directory CSVs_EVPN_MLAG ; \
	fi

.PHONY: clab_deploy
clab_deploy: ## Deploy ceos lab
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		sudo containerlab deploy --debug --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml --max-workers 2 --timeout 5m ;\
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v /etc/sysctl.d/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest sudo containerlab deploy --debug --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml --max-workers 2 --timeout 5m ;\
	fi

.PHONY: clab_destroy
clab_destroy: ## Destroy ceos lab
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		sudo containerlab destroy --debug --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml --cleanup ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v /etc/sysctl.d/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			test_clab:latest sudo containerlab destroy --debug --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml --cleanup ; \
	fi

.PHONY: clab_graph
clab_graph: ## Build lab graph
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		sudo containerlab graph --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml ;\
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v /etc/sysctl.d/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest sudo containerlab graph --topo $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}/clab/$(CLAB_NAME).clab.yml ;\
	fi

.PHONY: clean
clean: ## Remove all containerlab files and directories
	sudo rm -rf $(AVD_REPOSITORY_NAME); sudo rm .cookiecutters/cookiecutter.json

.PHONY: rm
rm: clean ## Remove all containerlab files and directories

.PHONY: onboard
onboard: ## onboard devices to CVP
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		$(CURRENT_DIR)/onboard_devices_to_cvp.py ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR) \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest $(CURRENT_DIR)/onboard_devices_to_cvp.py ; \
	fi

.PHONY: avd_build_eapi
avd_build_eapi: ## build configs and configure switches via eAPI
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		cd $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}; ansible-playbook playbooks/fabric-deploy-eapi.yml ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR)/${AVD_REPOSITORY_NAME} \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest ansible-playbook playbooks/fabric-deploy-eapi.yml ; \
	fi

.PHONY: avd_build_cvp
avd_build_cvp: ## build configs and configure switches via eAPI
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		cd $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}; ansible-playbook playbooks/fabric-deploy-cvp.yml ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR)/${AVD_REPOSITORY_NAME} \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest ansible-playbook playbooks/fabric-deploy-cvp.yml ; \
	fi

.PHONY: avd_validate
avd_validate: ## build configs and configure switches via eAPI
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		cd $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}; ansible-playbook playbooks/validate-states.yml ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR)/${AVD_REPOSITORY_NAME} \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest ansible-playbook playbooks/validate-states.yml ; \
	fi

.PHONY: avd_snapshot
avd_snapshot: ## build configs and configure switches via eAPI
	if [ "${_IN_CONTAINER}" = "True" ]; then \
		cd $(CURRENT_DIR)/${AVD_REPOSITORY_NAME}; ansible-playbook playbooks/snapshot.yml ; \
	else \
		docker run --rm -it --privileged \
			--network host \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v /etc/hosts:/etc/hosts \
			--pid="host" \
			-w $(CURRENT_DIR)/${AVD_REPOSITORY_NAME} \
			-v $(CURRENT_DIR):$(CURRENT_DIR) \
			-v $(CURRENT_DIR)/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
			-e AVD_GIT_USER="$(shell git config --get user.name)" \
			-e AVD_GIT_EMAIL="$(shell git config --get user.email)" \
			$(DOCKER_NAME):latest ansible-playbook playbooks/snapshot.yml ; \
	fi
