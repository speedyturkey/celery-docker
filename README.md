## Generic Dockerized Celery App

This repo contains a bare bones implemenation of a scheduled reporting application using Porthole, Celery, and Docker.
The application contains 3 tasks, each scheduled to run once per minute and print a statement to the console. 

### Get Started

In order to run the app, follow these steps. First, ensure that docker and docker-compose are installed on your machine.
Next, clone this repository and create the necessary configuration files:

- porthole.ini
    - This is the standard Porthole config file.
    - Bear in mind that all paths will be in the context of the docker container, and cannot reference directories
        on the host machine unless they are mounted inside the container.
- .env
    - This is a docker configuration file used to populate the variables inside docker-compose.yml.
    - Variables are in the format ${VAR_NAME}.
    - Specific variables will ultimately depend on project needs. This project requires:
        - PORTHOLE_CONFIG:  The location of the aforementioned porthole.ini file (inside the container).
        - REPORT_PATH: The path on your host machine where report files will be written. This path will be mounted
            inside the container. Note that you will still need to reference this path in your porthole config.

To build your docker image, you will first need to ensure that you have the necessary deploy key. Then, execute the 
following docker build command:

`docker-compose build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/DataTeam-deploy-key)"`

### Application Components

Here is an overview of the application structure.

    .
    ├── application             # Contains all of your Python code
    │   ├── reports             #
    │       ├── samples.py      # Task definitions    
    │   ├── __init__.py         # Instantiate application
    │   ├── celery.py           # Finalizes application setup and sets schedule
    │   └── celeryconfig.py     # Key application configuration variables
    │   └── porthole.ini        # Standard Porthole config file
    │   └── tasks.py            # Defines task manifest and helps setup task schedule   
    ├── .env                    # Variables for processing docker-compose.yml
    ├── .gitignore              # Standard .gitignore
    ├── docker-compose.yml      # Defines your docker containers.
    ├── dockerfile              # Builds your base docker image. 
    ├── README.md               # This document!
    └── requirements.txt        # Used to install Python dependencies into the docker containers.





References and Notes

- Docker Configuraion
    - https://vsupalov.com/docker-arg-env-variable-guide/
- Python Dependency Notes
    - There are some difficulties getting pandas to work inside a docker container. There is some useful reference material available here: https://github.com/amancevice/docker-pandas/blob/master/alpine/Dockerfile
- Useful information on redis performance:
    - https://www.techandme.se/performance-tips-for-redis-cache-server/
- Useful information on installing private Python packages inside a docker container:
    - https://github.com/bmihelac/docker-images-with-private-python-packages-example/blob/master/Dockerfile-deploykeys


