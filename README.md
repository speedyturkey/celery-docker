Docker build command:

`docker-compose build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/DataTeam-deploy-key)"`

Python Dependency Notes

There are some difficulties getting pandas to work inside a docker container. There is some useful reference material available here: https://github.com/amancevice/docker-pandas/blob/master/alpine/Dockerfile

Useful information on redis performance:

https://www.techandme.se/performance-tips-for-redis-cache-server/

Useful information on installing private Python packages inside a docker container:

https://github.com/bmihelac/docker-images-with-private-python-packages-example/blob/master/Dockerfile-deploykeys