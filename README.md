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

`sudo docker run -p 8888:5000 rf-api` to run a docker and map from port 5000 (container) to port 8888 localhost of host machine

## Building production grade Docker application
Until now we only started a flask development server in our Docker application. This is nice for development but does not scale enough for production.

### Docker deployment with flask
We will use an industry grade webserver to host our flask application.

1. Apache
2. Nginx

These servers are meant to be webservers and are expected to *scale* regardless of number of current users.

Flask is not advisable for production.

We need to build a bridge between our python app *Flask* and a mature webserver like *Apache* called **WSGI** (Webserver Gateway Interface). 

End-user or software will hit the webserver with requests. Apache will *split* those requests. You have to provision for the number of concurrent users. Apache can handle all that with the right underlying hardware by consuming, coordinating and routing them through WSGI to our Flask application. Flask runs the machine learning predictor, sends back the results through WSGI to Apache which sends the results to the end-user.

You have to also install the python module `mod_wsgi` (into `requirements.txt`.

### Writing the wsgi file
Same name as python script with `.wsgi` suffix.
Needs to know the exact python environment and the exact python object that contains the app.

Note that the port specified in flask is only the development server. Will be overriden by Apache web server port specified in Dockerfile.

Create the image and then launch a container that leverages this image:

`docker run -d -p 8888:8000 apache-flask`

### Debugging Docker container
Attach your terminal to the docker containers terminal:
`docker exec -it <id> bash` (find out id with `docker ps`)

Check apaches logs: `emacs /etc/mod_wsgi-express-80/error_log`

### Removing all unused images
`sudo docker prune`

## Quiz
1. In Docker, a union file system is the union of read-write layer and all read-only layers
2. Docker Images have different states and keep changing with time. False
3. In what format are Docker images identified? 64 hexadecimal digit string
4. Which of the following is True? In Docker, when a container is exited. The state of the filesystem is stored but the processes are not.
5. What is the command used to convert a container into an image? docker commit
6. The default registry is accessible using the command: sudo docker search
7. Which of the following command is used to associate an image with a repository (or multiple repositories) at build time? sudo docker build -t NAME
8. docker ps shows all *running* containers by default.
9. By default, in what mode do Docker containers run in? And what is the value of the -d option that specifies the mode in which docker container runs? foreground mode; -d = True
10. docker diff command has 3 events listed in it: A-Add, D-Delete, C-Change