# use AVD all-in-one container to get all AVD requirements
FROM avdteam/avd-all-in-one:avd3.1.0_cvp3.2.0_debian

COPY requirements.txt /tmp/pip-tmp/requirements.txt
WORKDIR /tmp/pip-tmp/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && sudo rm -rf /tmp/pip-tmp

RUN sudo bash -c "$(curl -sL https://get-clab.srlinux.dev)" -- -v 0.23.0

# add aliases for quick lab access
# TODO: make it dynamic in future
RUN echo "alias spine1='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@spine1'">> ${HOME}/.zshrc \
    echo "alias spine2='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@spine2'">> ${HOME}/.zshrc \
    echo "alias leaf1='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@leaf1'">> ${HOME}/.zshrc \
    echo "alias leaf2='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@leaf2'">> ${HOME}/.zshrc \
    echo "alias leaf3='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@leaf3'">> ${HOME}/.zshrc \
    echo "alias leaf4='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@leaf4'">> ${HOME}/.zshrc \
    echo "alias border1='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@border1'">> ${HOME}/.zshrc \
    echo "alias border2='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@border2'">> ${HOME}/.zshrc \
    echo "alias host11='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@host11'">> ${HOME}/.zshrc \
    echo "alias host12='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@host12'">> ${HOME}/.zshrc \
    echo "alias host21='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@host21'">> ${HOME}/.zshrc \
    echo "alias host22='sshpass -p arista123 ssh -o \"StrictHostKeyChecking no\" cvpadmin@host22'">> ${HOME}/.zshrc

WORKDIR /home/avd/projects
