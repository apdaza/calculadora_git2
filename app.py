from flask import Flask, render_template, request
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/')
def hola():
    return render_template('calculadora.html')

@app.route('/suma/<int:valor_1>/<int:valor_2>')
def suma(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.sumar()
    return str(c.resultado)

@app.route('/resta/<int:valor_1>/<int:valor_2>')
def resta(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.restar()
    return str(c.resultado)

@app.route('/multiplicacion/<int:valor_1>/<int:valor_2>')
def multiplicacion(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.multiplicar()
    return str(c.resultado)

def division(valor_1, valor_2):
    c = Calculadora()
    c.valor_1 = valor_1
    c.valor_2 = valor_2
    c.dividir()
    return int(c.resultado)

@app.route('/operacion/<operador>/<int:valor_1>/<int:valor_2>', methods = ['POST', 'GET'])
def operacion(operador, valor_1, valor_2):
    if request.method == 'POST':
        if operador == "sumar":
            resultado =  suma(valor_1, valor_2)
        elif operador == "restar":
            resultado =  resta(valor_1, valor_2)
        elif operador == "multiplicar":
            resultado =  multiplicacion(valor_1, valor_2)
        elif operador == "dividir":
            resultado =  division(valor_1, valor_2)
        else:
            resultado = hola()
        return render_template('calculadora.html', resultado = resultado)
    else:
        return render_template('calculadora.html')

    


if __name__ == '__main__':
    app.run(debug = True)