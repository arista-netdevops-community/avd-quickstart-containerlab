# use AVD all-in-one container to get all AVD requirements
FROM avdteam/avd-all-in-one:latest

COPY requirements.txt /tmp/pip-tmp/requirements.txt
WORKDIR /tmp/pip-tmp/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && sudo rm -rf /tmp/pip-tmp

# add aliases for quick lab access
# TODO: make it dynamic in future
RUN alias leaf1='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@leaf1' \
    alias leaf2='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@leaf2' \
    alias leaf3='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@leaf3' \
    alias leaf4='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@leaf4' \
    alias border1='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@border1' \
    alias border2='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@border2' \
    alias spine1='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@spine1' \
    alias spine2='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@spine2' \
    alias host11='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@host11' \
    alias host12='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@host12' \
    alias host21='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@host21' \
    alias host22='sshpass -p arista123 ssh -o "StrictHostKeyChecking no" cvpadmin@host22'

WORKDIR /home/avd/projects
