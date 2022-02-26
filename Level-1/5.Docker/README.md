# ![alt text](https://carteblanche.tech/static/static/website/images/general/logo.svg "Logo Title")  &nbsp; &nbsp;  PART 5 - DOCKER

This README file contains DOCKER based questions which is used to setup backend environment for Python.

### Question No 1:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1. Compare different kind of docker image families. Alpine, Slim, Stretch, Buster, Jessie, Bullseye. What does these mean ? How are they different? What advantage they provide over the others?

### Answer No 1:
| Alpine                                                             | Slim                                                             | Stretch                                                          | Buster                                                           | Jessie                                                           | Bullseye                                                         |
|--------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Alpine is a Linux based distribution. It has a very compact size   | Alpine is a Linux based distribution. It has a very compact size | Alpine is a Linux based distribution. It has a very compact size | Alpine is a Linux based distribution. It has a very compact size | Alpine is a Linux based distribution. It has a very compact size | Alpine is a Linux based distribution. It has a very compact size |
|                                                                    |                                                                  |                                                                  |                                                                  |                                                                  |                                                                  |
|                                                                    |                                                                  |                                                                  |                                                                  |                                                                  |                                                                  |

<br />

### Question No 2:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Difference between Entry point and CMD directive in a Dockerfile?

### Answer No 2:


Both CMD and ENTRYPOINT are two important directives in a Dockerfile. 
1. ENTRYPOINT is the command we run when container starts. CMD is used when a container starts or is specified by CMD we give an argument to ENTRYPOINT. 
2. CMD can be overridden but we cannot override ENTRYPOINT unless we specify the --entrypoint flag in the configuration when starting the container.
3. We define ENTRYPOINT when executing the container. We use CMD as the configuration of default arguments for an ENTRYPOINT command.
<br />

### Question No 3:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Explain this command written inside a Dockerfile:RUN mkdir /app/django/helloworld

### Answer No 3:

When this command Dockerfile:RUN mkdir /app/django/helloworld will be executed it will create a directory named helloworld inside the directory of /app/django.

<br />

### Question No 4:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Explain the concept of layering in docker images/containers?

### Answer No 4:

There are a total of 4 layers inside a docker image/container. The first layer is called as Base Image/ Ubuntu OS. The 2nd layer is the update packages layer. The 3rd layer is the configure application server the 4th layer is the container layer accessible to the user. Only Layer 4 is Read/Write allowed layer the below 3 layers are read only layer. Each layer is an image. Every single instruction in a Dockerfile results in a layer. 