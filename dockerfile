FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./projekt /projekt
# create celery user/group and set perms
RUN addgroup -S celery
RUN adduser -S celery -s /bin/sh -G celery
RUN mkdir /var/log/celery /var/run/celery
RUN chown -R celery:celery /var/run/celery/ /var/log/celery/
