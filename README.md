# AVD Quickstart Containerlab

> **WARNING**  
> Please read the guide before you start using AVD Quickstart Containerlab.
> Make sure that you understand the consequences of running Containerlab, cEOS-lab and various scripts provided with this repository on your machine. The components of the lab may change your system settings as they will have super user privileges.
> While this repository was tested on a number of machines without doing any harm, have a plan B. You are responsible for your lab machine, not the contributors.
>
> `"With su power comes great responsibility" (c)`
>
> ```text
>   /  _  \
> \_\_(_)_/_/
>  _/ /o\ \_
>    /   \
> ```

**For M1 MacBooks owners**:  
> Sorry. Not yet supported.

- [AVD Quickstart Containerlab](#avd-quickstart-containerlab)
  - [Overview](#overview)
  - [Lab Requirements](#lab-requirements)
  - [Release Notes:](#release-notes)
  - [How To Use The Lab](#how-to-use-the-lab)
  - [How To Destroy The Lab](#how-to-destroy-the-lab)

## Overview

The AVD Quickstart repository is a collection of Arista EOS labs based on [Containerlab](https://containerlab.srlinux.dev/) that you can build on any machine with Docker in a few minutes.
The ultimate target of this repository is to provide a **portable Arista lab collection** for everyone. This collection can be used to learn and test certain Arista EOS features and in certain cases even build configs for production environment with the excemption of hardware features.

Some labs provided in this repository can be used with CloudVision Portal VM that must be deployed separately. But all labs that are not focused on CVP features can be used without such VM as it is quite resource intensive and can not be deployed on an avarage laptop for example.

> **WARNING**: if CVP VM is part of the lab, make sure that it's reachable and credentials configured on CVP are matching the lab.

The initial lab list provided in this repository is focused on learning and testing [AVD](https://avd.sh/en/latest/).
Some labs can be easily adjusted to your needs using simplified CSV and YAML inputs.

Currently following labs are available:

- AVD repository to build EVPN MLAG network
- AVD repository to build EVPN Active-Active network

## Lab Requirements

A machine with Docker CE or Docker Desktop is required.
Following operating systems were tested:

- Ubuntu LTS Server
- MacOs (on x86 laptops only)
The lab is expected to run on any major Linux distribution.
Please test and contribute by reporting and/or fixing possible issues.

Hardware requirements depend on the number of containers deployed. Please read [Containerlab Scalability with cEOS](#containerlab-scalability-with-ceos) section before deploying a large topology.
For a small topology of 10+ cEOS containers 8 vCPUs and 10 GB RAM are recommended.

> **WARNING**: Please make sure that your host has enough resorces. Otherwise Containerlab can enter "frozen" state and require Docker restart.

To install Docker on a Linux machine, check [this guide](https://docs.docker.com/engine/install/ubuntu/).
To get Docker Desktop, check [docker.com](https://www.docker.com/products/docker-desktop/).

If you are planning to deploy Containerlab on a dedicated Linux host, you can also install and configure KVM and deploy CloudVision Portal as a virtual machine. To install KVM, check [this guide](https://github.com/arista-netdevops-community/kvm-lab-for-network-engineers) or any other resource available on internet. Once KVM is installed, you can use one of the following repositories to install CVP:
- ISO-based KVM installer - currently not available on Github and distributed under NDA only. That will be fixed later.
- [CVP KVM deployer](https://github.com/arista-netdevops-community/cvp-kvm-deployer)
- [CVP Ansible provisioning](https://github.com/arista-netdevops-community/cvp-ansible-provisioning)

It is also possible to run CVP on a dedicated host and a different hypervisor as long as it can be reached by cLab devices.

> NOTE: to use CVP VM with container lab it's not required to recompile Linux core. That's only required if you plan to use vEOS on KVM for you lab setup.

The lab setup diagram:

![lab diagram](media/lab_setup.png)

## Release Notes:

- **0.1**
  - initial release with many shortcuts
- **0.2**
  - Fix bugs.
  - Improve lab topology.
  - Improve lab workflow.
  - Add EVPN AA scenario.
- **0.3**
  - The lab now only requires Docker. Containerlab installation is not required and will be running inside provided Docker container.
  - When building container with `make build`, UID and GID will be updated using intermediate container similar to the container used by VSCode devcontainers.
  - The Dockerfile can be used as VSCode devcontainer or standalone.
  - The lab environment is now supported and tested on MacOS. x86 MacBooks only.
  - Dynamic aliases in the container for quick access to lab devices.

## How To Use The Lab

1. Clone this repository to your lab host: `git clone https://github.com/arista-netdevops-community/avd-quickstart-containerlab.git`
2. It is recommended to remove git remote as changes are not supposed to be pushed to the origin: `git remote remove origin`
3. Change to the lab directory: `cd avd-quickstart-containerlab`
4. Before running the lab it is recommended to create a dedicated git branch for you lab experiments to keep original branch clean.
5. Check makefile help for the list of commands available: `make help`

```zsh
petr@nuc10i7:~/avd-quickstart-containerlab$ make help
avd_build_cvp                  build configs and configure switches via eAPI
avd_build_eapi                 build configs and configure switches via eAPI
build                          Build docker image
clab_deploy                    Deploy ceos lab
clab_destroy                   Destroy ceos lab
clab_graph                     Build lab graph
help                           Display help message
inventory_evpn_aa              onboard devices to CVP
inventory_evpn_mlag            onboard devices to CVP
onboard                        onboard devices to CVP
rm                             Remove all containerlab directories
run                            run docker image. This requires cLab "custom_mgmt" to be present
```

4. If you don't have cEOS image on your host yet, download it from arista.com and import. Make sure that image name is matching the parameters defined in `CSVs_EVPN_AA/clab.yml` or `CSVs_EVPN_MLAG/clab.yml`
5. Use `make build` to build `avd-quickstart:latest` container image. If that was done earlier and the image already exists, you can skip this step.
6. Run `make inventory_evpn_aa` or `make inventory_evpn_mlag` to build the inventory for EVPN AA or MLAG scenario. Ideally AVD inventroy must be a different repository, but for simplicity script will generate inventory in the current directory.
7. Review the inventory generated by avd-quickstart. You can optionally git commit the changes.
8. Run `make clab_deploy` to build the containerlab. Wait until the deployment will finish.
9. Execute `make run` to run `avd-quickstart` container.
10. If CVP VM is used in the lab, onboard cLab switches with `make onboard`. Once the script behind this shortcut wil finish, devices will appear in the CVP inventory.
11. To execute Ansible AVD playbook, use `make avd_build_eapi` or `make avd_build_cvp` shortcuts. That will execute `playbook/fabric-deploy-eapi.yml` or `playbook/fabric-deploy-cvp.yml`.
12. Run `make avd_validate` to execute AVD state validation playbook `playbooks/validate-states.yml`.
13. Run `make avd_snapshot` if you want to collect a network snapshot with `playbooks/snapshot.yml`.
14. Connect to hosts and switches and run some pings, show commands, etc. To connect to a lab device, you can type it's hostname in the container:

![connect to a device from the container](media/connect-to-device.png)

> NOTE: device hostnames are currently hardcoded inside the `avd-quickstart` container. If you have customized the inventory, ssh to the device manually. That will be improved in the coming versions.

You can optionally git commit the changes and start playing with the lab. Use CSVs to add some VLANs, etc. for example. Re-generate the inventory and check how the AVD repository data changes.

## How To Destroy The Lab

1. Exit the `avd-quickstart` container by typing `exit`
2. Execute `make clab_destroy` to destroy the containerlab.
3. Execute `make rm` to delete the generated AVD inventory.
