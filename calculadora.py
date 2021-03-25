class Calculadora:
    """clase para las operaciones básicas"""

    def __init__(self):
        self.valor_1 = 0
        self.valor_2 = 0
        self.resultado = 0

    def sumar(self):
        """operación que suma los valores seteados en la calculadora"""
        self.resultado = self.valor_1 + self.valor_2

    def restar(self):
        """operación que resta los valores seteados en la calculadora"""
        self.resultado = self.valor_1 - self.valor_2

    def multiplicar(self):
        """operación que multiplica los valores seteados en la calculadora"""
        pass

    