from flask import Flask, __version__ 
app = Flask(__name__)

@app.route('/')
def hello_world():
   return f'Hello World (flask version {__version__})'

if __name__ == '__main__':
   app.run()

