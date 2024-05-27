class Classe:
    def __init__(self):
        self.nome = None
        self.habilidades = {}
        
    
    def __str__(self):
        return(f'{self.nome}')
    
    def adicionar_habilidade(self, habilidades):
        for habilidade, valores in habilidades.items():
            self.habilidades[habilidade] = valores