# Docker
## Comparison to VMs
A virtual machine sits on top of hardware and has its own "copy" of CPU, memory, storage, and network. Even if the VM is idling, these resources are bound.
This leads to under utilization of hardware.

Docker is a virtualization ontop of operating system, not the physical resources! Has its own PID, network stack and root file system.

More dynamic than VMs. If you have 4 containers and 3 are idle, the last one can utilize more resources.

## Comparison to conda or python environments

Conda envs isolate well too but Docker is more portable. Reproducability of environment leads to reproducability of output.

## Get vs Post requests

* Get request: parameters in url
* Post request: more secure since not in url. Use app like postman (see file `flask2_post.py`)

## Url name
* `@app.route('/')` => `http://127.0.0.1:7000/`
* `@app.route('/url_name')` => `http://127.0.0.1:7000/url_name`

## Summary
Things you have to keep in mind in order to expose your functionalities as an API:

1. import flask
2. initialize the app
3. in our main program run the app maybe with custom port
4. Decide wheter get (`flask1.py`) or post request (`flask2_post.py`)

## UI with flasgger

## Build a Docker container
Image might look like this:

* flask, flasgger and
* Anaconda on
* Linux (Base image)

Important commands:

1 `from` (specifies the base image)
2. `copy` (copies a list of files or folders from the host device to docker image)
3. `expose` (opens ports of the docker image)
4. `workdir` (specify the work container of the work when it starts, every command you run, will be executed here, no need to cd here)
5. `run` (every command you specify after run will run inside of your docker container, use only *one* RUN command to save storage space! Do a new line with \ &&)
6. `cmd` (specifies the last command that runs forever)

Hint: use *continuumio/anaconda* as base image as it already contains a good python distro with machine learning libraries

### Dockerfile
```
FROM continuum/anaconda
COPY hfs(host_file_sys)/flask_model_folder /usr/local/flask_model_folder
EXPOSE 5000
WORKDIR /usr/local/flask_model_folder
RUN pip install needed_libraries
CMD python flask_app.py
```
### Build image

`sudo docker build -t name .`


`docker ps` to look at your running containers

`docker images` to look at your images

`sudo docker run -p 8888:5000 rf-api` to run a docker