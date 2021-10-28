CURRENT_DIR = $(shell pwd)
BRANCH ?= $(shell git symbolic-ref --short HEAD)
PYTHON = $(shell python3 --version)

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
