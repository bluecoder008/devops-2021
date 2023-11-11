# README
This folder contains the code to demonstrate how to

## Containerize Python Applications using Docker
- `<Install python3>`
- Install flask package
  -   <code>$ pip3 install -U Flask</code> 
- Create the simple (but super-cool) python3 app
  - <code>$ cat my_app.py</code>
```
    from flask import Flask, __version__ 
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
       return f'Hello World (flask version {__version__})'

    if __name__ == '__main__':
       app.run(host='0.0.0.0')
```
- Construct the Dockerfile
  - <code>$ cat Dockerfile</code>
```
    FROM python3:8

    ADD my_app.py .

    RUN pip3 install -U Flask

    CMD ["python3", "my_app.py"]
```
- Build the docker image
  - $<code>docker build . -t 2021devops/my_python_app</code>																	
- [optional] Push the docker image
  - $<code>docker push 2021devops/my_python_app</code>
- Run the docker image
  - $<code>docker run -d -p 5000:5000 -it 2021devops/my_python_app</code>
- Verify the Dockerized app running as expected
  - $<code>oprn http://localhost:5000</code>
#### Trouble-shooting notes
- To start `bash` session inside the docker container
  ```
    $ docker ps  # inspect container listing and get the container id
    CONTAINER ID   IMAGE           COMMAND              CREATED         STATUS         PORTS                    NAMES
    a3503b07e6a3   my_python_app   "python my_app.py"   7 seconds ago   Up 6 seconds   0.0.0.0:5000->5000/tcp   condescending_sinoussi

    $ docker exec -it a3503b07e6a3 bash
    root@a3503b07e6a3:/#
  ```
