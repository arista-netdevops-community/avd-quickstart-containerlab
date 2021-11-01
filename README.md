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
- ISO-based KVM installer

> NOTE: to use CVP VM with container lab it's not required to recompile Linux core. That's only required if you plan to use vEOS on KVM for you lab setup.

The lab setup diagram:

<tbd>

## How To Use The Lab

1. Clone this repository to your lab host: `git clone https://github.com/arista-netdevops-community/avd-quickstart-containerlab.git`
2. Change to the lab directory: `cd avd-quickstart-containerlab`
3. Check makefile help for the list of commands available: `make help`

```bash
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

4. Create AVD container lab: `make deploy`