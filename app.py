from flask import Flask
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/')
def hola():
    return 'Hola mundo'

@app.route('/suma/<int:valor_1>/<int:valor_2>')
def suma(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.sumar()
    return str(c.valor_1) + " + " + str(c.valor_2) + " = " + str(c.resultado)

if __name__ == '__main__':
    app.run(debug = True)