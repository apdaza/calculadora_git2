from calculadora import Calculadora

c = Calculadora()

c.valor_1 = 2
c.valor_2 = 5

c.sumar()

print(str(c.valor_1) + " + " + str(c.valor_2) + " = " + str(c.resultado))