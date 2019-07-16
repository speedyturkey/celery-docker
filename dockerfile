FROM python:3.7-alpine

RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache --virtual .build-deps g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN apk update && apk add postgresql-dev gcc musl-dev
RUN apk add git
RUN apk add openssh
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN apk del .build-deps

RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf

ARG SSH_PRIVATE_KEY
RUN mkdir /root/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

RUN echo "Host data-team.github.com" >> /root/.ssh/config
RUN echo "HostName github.com" >> /root/.ssh/config
RUN echo "User git" >> /root/.ssh/config
RUN echo "IdentityFile ~/.ssh/id_rsa" >> /root/.ssh/config
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN pip install git+ssh://git@data-team.github.com/ARPC/DataTeam.git
RUN rm -rf /root/.ssh