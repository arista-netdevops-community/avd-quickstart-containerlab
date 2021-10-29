# aus AVD all-in-one container to get all AVD requirements
FROM avdteam/avd-all-in-one:latest

COPY requirements.txt /tmp/pip-tmp/requirements.txt
WORKDIR /tmp/pip-tmp/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && sudo rm -rf /tmp/pip-tmp

WORKDIR /home/avd/projects
