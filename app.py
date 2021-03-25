from flask import Flask
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/')
def hola():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug = True)