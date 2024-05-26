class Poderes:
    def __init__(self):
        self.lista = {}
    
    def adicionar(self, poderes):
        # poderes = {'Nome do Poder': {'usar': 'poder', 'palavras_chaves': ['ativa', 'passiva', 'humano']}}
        for poder, valores in poderes.items():
            self.lista[poder] = valores
            
    def remover(self, poderes):
        for poder in poderes:
            self.lista.pop(poder, None)
            
    def ativar_passivas(self):
        for valores in self.lista.values():
            valores['usar']() if 'passiva' in valores['palavras_chaves'] else ''
            