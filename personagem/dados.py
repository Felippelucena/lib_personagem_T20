from random import randint

class Dados:
    def rolar(self, quantidade=1, lados=6):
        return [randint(1,lados) for _ in range(quantidade)]
