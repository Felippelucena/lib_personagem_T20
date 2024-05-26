
class Atributos:
    def __init__(self, pontos=10):
        self.lista = {  'for': {'base':0 },
                        'des': {'base':0 },
                        'con': {'base':0 },
                        'int': {'base':0 },
                        'sab': {'base':0 },
                        'car': {'base':0 }  }
        self.pontos = pontos
        
        
    def definir(self, dados=None, atributos=None):
        if atributos == None:
            #ALEATORIO
            resultados = []
            converter = { -2: (7, 6, 5, 4, 3), -1: (8, 9), 0: (10, 11), 1: (12, 13), 2: (14, 15), 3: (16, 17), 4: (18) }
            while sum(resultados) < 6:
                for _ in range(6):
                    rolar_dados = sorted(dados.rolar(4, 6))[1:]  # rola 4d6, ordena e remove o menor valor
                    resultados.append(sum(rolar_dados))  # soma os valores restantes
                # Converter os resultados das rolagens usando o dicionário
                resultados = [
                    key if isinstance(valores, int) and valor == valores else key
                    for valor in resultados
                    for key, valores in converter.items()
                    if (isinstance(valores, tuple) and valor in valores)]
            for atributo, valor in zip(self.lista.keys(), resultados):
                self.lista[atributo]['base'] = valor 
            self.pontos = 0 
                           
        else:
            #ESCOLHER
            custo = { -1: 1, 0: 0, 1: -1, 2: -2, 3: -4, 4: -7 }
            if self.pontos == 10:
                self.pontos += sum(custo[atributo] for atributo in atributos.values())
                
                if self.pontos == 0:
                    for atributo, valor in atributos.items():
                        self.lista[atributo]['base'] = valor
                else:
                    self.pontos = 10
    
    def __str__(self):
        atributos = {}
        for atributo, valor in self.lista.items():
            atributos[atributo] = sum(valor.values())
        return f'{atributos}'
    
    def obj(self):
        atributos = {}
        for atributo, valor in self.lista.items():
            atributos[atributo] = sum(valor.values())
        return atributos
    
    def adicionar_mod(self, palavra_chave, atributos):
        for atributo, valor in atributos.items():
            self.lista[atributo][palavra_chave] = valor
