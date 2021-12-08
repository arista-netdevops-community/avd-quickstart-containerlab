#!/bin/bash
mkdir -p clab-{{ cookiecutter.in.clab.name }}
{% for a_switch in cookiecutter.out.clab_mac_address %}
mkdir -p clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}
mkdir -p clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}/flash
echo "SYSTEMMACADDR={{ a_switch.mac_address }}" > clab-{{ cookiecutter.in.clab.name }}/{{ a_switch.hostname }}/flash/ceos-config
{% endfor %}