class Poderes:
    def __init__(self):
        self.lista = {}
        
        
    def __str__(self):
        return f"{self.nome}: {self.descricao} (Palavras-chave: {', '.join(self.palavras_chaves)})"
    def adicionar(self, poderes):
        # poderes = {'Nome do Poder': {'usar': 'poder', 'palavras_chaves': ['ativa', 'passiva', 'humano']}}
        for poder, valores in poderes.items():
            self.lista[poder] = valores
            
    def remover(self, poderes):
        for poder in poderes:
            self.lista.pop(poder, None)