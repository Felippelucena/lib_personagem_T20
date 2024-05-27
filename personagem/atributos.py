class Atributos:
    def __init__(self):
        self.pontos = 10
        self.lista = {  'for': {'base':0 },
                        'des': {'base':0 },
                        'con': {'base':0 },
                        'int': {'base':0 },
                        'sab': {'base':0 },
                        'car': {'base':0 }  }
        

    def __str__(self):
            return str({atributo: sum(valor.values()) for atributo, valor in self.lista.items()})

    def total(self):
            return {atributo: sum(valor.values()) for atributo, valor in self.lista.items()}

    
    def adicionar_mod(self, palavra_chave, atributos):
        for atributo, valor in atributos.items():
            self.lista[atributo][palavra_chave] = valor

    def atributos_minimos(self):
        descricao = 'Um valor menor que –5 em um atributo gera um efeito: For ou Des (paralisado), Con (morre), Int ou Sab (inconsciente), Car (torna-se um NPC). Issoignora imunidades. Ver livro básico Tormenta 20 pag 17.'
        return descricao