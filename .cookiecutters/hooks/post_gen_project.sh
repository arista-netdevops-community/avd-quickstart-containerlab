#!/bin/bash
mkdir -p clab-{{ cookiecutter.in.clab.name }}
{% for a_switch in cookiecutter.out.clab_mac_address %}
mkdir -p clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}
mkdir -p clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}/flash
echo "SYSTEMMACADDR={{ a_switch.mac_address }}" > clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}/flash/ceos-config
{% endfor %}
# add zsh aliases for convinient ssh to clab containers
echo "#!/usr/bin/zsh" > /home/avd/.oh-my-zsh/custom/aliases.zsh
chmod +x /home/avd/.oh-my-zsh/custom/aliases.zsh
{% for avd_device in cookiecutter.in.inventory %}
echo "alias {{ avd_device.hostname }}='sshpass -p {{ cookiecutter.in.avd_mgmt.cvp_password }} ssh -o \"StrictHostKeyChecking no\" {{ cookiecutter.in.avd_mgmt.cvp_username }}@clab-{{ cookiecutter.in.avd_general.avd_repository_name }}-{{ avd_device.hostname }}'" >> /home/avd/.oh-my-zsh/custom/aliases.zsh
{% endfor %}
{% for non_avd_device in cookiecutter.in.non_avd_inventory %}
echo "alias {{ non_avd_device.hostname }}='sshpass -p {{ cookiecutter.in.avd_mgmt.cvp_password }} ssh -o \"StrictHostKeyChecking no\" {{ cookiecutter.in.avd_mgmt.cvp_username }}@clab-{{ cookiecutter.in.avd_general.avd_repository_name }}-{{ non_avd_device.hostname }}'" >> /home/avd/.oh-my-zsh/custom/aliases.zsh
{% endfor %}
exec zsh