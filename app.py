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

@app.route('/resta/<int:valor_1>/<int:valor_2>')
def resta(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.restar()
    return str(c.valor_1) + " - " + str(c.valor_2) + " = " + str(c.resultado)

@app.route('/multiplicacion/<int:valor_1>/<int:valor_2>')
def multiplicacion(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.multiplicar()
    return str(c.valor_1) + " * " + str(c.valor_2) + " = " + str(c.resultado)

@app.route('/division/<int:valor_1>/<int:valor_2>')
def division(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.dividir()
    return str(c.valor_1) + " / " + str(c.valor_2) + " = " + str(c.resultado)

@app.route('/operacion/<operador>/<int:valor_1>/<int:valor_2>')
def operacion(operador, valor_1, valor_2):
    if operador == "+":
        return suma(valor_1, valor_2)
    elif operador == "-":
        return resta(valor_1, valor_2)
    elif operador == "*":
        return multiplicacion(valor_1, valor_2)
    elif operador == "d":
        return division(valor_1, valor_2)
    else:
        return hola()


if __name__ == '__main__':
    app.run(debug = True)