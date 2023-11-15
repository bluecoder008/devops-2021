from flask import Flask, __version__ 
app = Flask(__name__)

@app.route('/ok')
def hello_world():
   return f'Hello World (flask version {__version__})'

@app.route('/')
def hello_world0():
   return 'Hello World'

if __name__ == '__main__':
   app.run(host='0.0.0.0')

