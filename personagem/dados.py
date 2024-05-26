from random import randint

class Dados:
    def rolar(self, quantidade=1, lados=6):
        resultados = [randint(1,lados) for _ in range(quantidade)]
        return resultados