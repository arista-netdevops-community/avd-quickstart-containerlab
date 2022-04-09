#!/bin/bash

{% for a_ceos_container in cookiecutter.in.inventory %}
alias {{ a_ceos_container.hostname }}='sshpass -p {{ cookiecutter.in.avd_mgmt.cvp_password }} ssh -o "StrictHostKeyChecking no" {{ cookiecutter.in.avd_mgmt.cvp_username }}@{{ a_ceos_container.management_ip.split('/')[0] }}'
{% endfor %}
{% for a_ceos_container in cookiecutter.in.non_avd_inventory %}
alias {{ a_ceos_container.hostname }}='sshpass -p {{ cookiecutter.in.avd_mgmt.cvp_password }} ssh -o "StrictHostKeyChecking no" {{ cookiecutter.in.avd_mgmt.cvp_username }}@{{ a_ceos_container.management_ip.split('/')[0] }}'
{% endfor %}