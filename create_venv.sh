#!/bin/bash
sudo sudo apt install python3.9
sudo apt install python3.9-venv
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
shopt -s expand_aliases
alias venv="source .venv/bin/activate"