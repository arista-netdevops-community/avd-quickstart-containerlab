# AVD Quickstart Containerlab

> **WARNING**
> This repository is still under construction. It's fully functional, but has number of limitations.
> For example:
> - README is still work-in-progress
> - Lab configuration and adresses are hardcoded and have to be redefined in many different files if you setup is different. That will be simplified before the final release.
> - Some workflow and code optimization required.

- [AVD Quickstart Containerlab](#avd-quickstart-containerlab)
- [Overview](#overview)
  - [Release Notes:](#release-notes)
  - [Lab Prerequisites](#lab-prerequisites)
  - [How To Use The Lab](#how-to-use-the-lab)

# Overview

This repository helps to build your own [AVD](https://avd.sh/en/latest/) test lab based on [Containerlab](https://containerlab.srlinux.dev/) in minutes.
The main target is to simplify learning and testing AVD.
The lab can be used together with CVP VM deployed on KVM, but it's not mandatory.

## Release Notes:

- **0.1**
  - initial release with many shortcuts

## Lab Prerequisites

The lab requires a single Linux host (Ubuntu server recommended) with [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Containerlab](https://containerlab.srlinux.dev/install/) installed.
It's possible to run [Containerlab on MacOS](https://containerlab.srlinux.dev/install/#mac-os), but that was not tested. Dedicated Linux machine still looks like the most feasible option.

To test AVD with CVP, KVM can be installed on the same host. To install KVM, check [this guide](https://github.com/arista-netdevops-community/kvm-lab-for-network-engineers) or any other resource available on internet. Once KVM is installed, you can use one of the following repositories to install CVP:
- ISO-based KVM installer - currently not available on Github and distributed under NDA only. That will be fixed later.
- [CVP KVM deployer](https://github.com/arista-netdevops-community/cvp-kvm-deployer)
- [CVP Ansible provisioning](https://github.com/arista-netdevops-community/cvp-ansible-provisioning)

> NOTE: to use CVP VM with container lab it's not required to recompile Linux core. That's only required if you plan to use vEOS on KVM for you lab setup.

The lab setup diagram:

![lab diagram](media/avd_quickstart.jpeg)

## How To Use The Lab

1. Clone this repository to your lab host: `git clone https://github.com/arista-netdevops-community/avd-quickstart-containerlab.git`
2. Change to the lab directory: `cd avd-quickstart-containerlab`
3. Before running the lab it is recommended to create a dedicated git branch for you lab experiments to keep original branch clean.
4. Check makefile help for the list of commands available: `make help`

```zsh
petr@nuc10i7:~/avd-quickstart-containerlab$ make help
build                          Build docker image
deploy                         Deploy ceos lab
destroy                        Destroy ceos lab
graph                          Build lab graph
help                           Display help message
inventory                      onboard devices to CVP
onboard                        onboard devices to CVP
rm                             Remove all containerlab directories
run                            run docker image
```

4. If you don't have cEOS image on your host yet, download it from arista.com and import.
5. Verify that `atd-quickstart.clab.yml` points to the correct image.
6. Create AVD container lab: `make deploy`
7. Build `avd-quickstart:latest` container image: `make build`. Skip this step if that was done earlier and image already exists.
8. Run the container: `make run`
9. If CVP is part of the lab, onboard cEOS devices with `make onboard` (in the container).
10. Build AVD inventory with Cookiecutter: `make inventory` (in the container). Ideally AVD inventroy must be a different repository, but for simplicity script will generate inventory in the current directory.
11. Change current directory to generated AVD repository (in the container): `cd avd_quickstart_inventory`
12. Run ansible-playbook to provision the lab (in the container): `ansible-playbook playbook/fabric-deploy-eapi.yml` or `ansible-playbook playbook/fabric-deploy-cvp.yml` (if CVP VM is part of the lab). Git commit generated configuration.
13. Run ansible-playbook to validate network state and check reports: `ansible-playbook playbook/validate-states.yml` Git commit generated files.
14. Run ansible-playbook to execute network snapshot commands: `ansible-playbook playbook/snapshot.yml` Git commit generated files.

Expeiment with changing files in `CSVs` directory, generate new inventory and repeat steps above to see the difference.
If something goes wrong and can not be fixed any more, destroy the lab with `make destroy` and create a new one.
