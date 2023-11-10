# README
This folder contains the code to demonstrate how to

## Containerize Python Applications using Docker
- `<Install python3>`
- Install flask package
  -   <code>$ pip3 install -U Flask</code> 
- Create the simple (but super-cool) app
  -   <code>$ cat my_app.py</code>```
from flask import Flask, __version__ 
app = Flask(__name__)

@app.route('/')
def hello_world():
   return f'Hello World (flask version {__version__})'

if __name__ == '__main__':
   app.run()
```


 
