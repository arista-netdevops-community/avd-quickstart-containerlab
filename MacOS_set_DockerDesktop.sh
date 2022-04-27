#!/bin/bash

# This cript helps to configure Docker Desktop on MacOS to work correctly with cEOS and ContainerLab
# The script is based on the following thread: https://github.com/docker/for-mac/issues/6073

# REQUIREMENTS:
# - Homebrew

# In case of problems try:
# - brew doctor
# Known issues:
# - problem with /usr/local/* ownership. To fix: cd /usr/local/; sudo chown -R $(whoami) *

# just in case your forgot to backup Docker Desktop settings
# if it's all broken, reset Docker Desktop settings
cp ~/Library/Group\ Containers/group.com.docker/settings.json docker_desktop_settings_$(date "+%Y.%m.%d-%H.%M.%S").json

# check if the list of running containers is empty and stop Docker Desktop using AppleScript
test -z "$(docker ps --quiet 2>/dev/null)" && osascript -e 'quit app "Docker"'

# if jq and moreutils are missing, install using homebrew
test -z "$(brew list | grep jq 2>/dev/null)" && brew install jq
test -z "$(brew list | grep moreutils 2>/dev/null)" && brew install moreutils

# enable cgroup v1 support - not required as of cEOS-lab 4.28.0F
# jq '.deprecatedCgroupv1 = true' ~/Library/Group\ Containers/group.com.docker/settings.json | sponge ~/Library/Group\ Containers/group.com.docker/settings.json
jq '.filesharingDirectories += ["/var/run/docker.sock"]' ~/Library/Group\ Containers/group.com.docker/settings.json | sponge ~/Library/Group\ Containers/group.com.docker/settings.json
jq '.filesharingDirectories += ["/etc/hosts"]' ~/Library/Group\ Containers/group.com.docker/settings.json | sponge ~/Library/Group\ Containers/group.com.docker/settings.json
# on MacOS /etc -> /private/etc
jq '.filesharingDirectories += ["/private/etc/hosts"]' ~/Library/Group\ Containers/group.com.docker/settings.json | sponge ~/Library/Group\ Containers/group.com.docker/settings.json

# add home path to sharing list as Docker Desktop on MacOS will be confused by internal container path otherwise
jq '.filesharingDirectories += ["/home"]' ~/Library/Group\ Containers/group.com.docker/settings.json | sponge ~/Library/Group\ Containers/group.com.docker/settings.json

# restart Docker Desktop
open --background -a Docker