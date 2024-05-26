from .poderes import Poderes_Racas

class Raca:
    def __init__(self):
        self.nome = None
        self.pericias = None
        self.poderes = {'ativas':{},'passivas':{}}
        
        
    def definir(self,raca, atributos=None, pericias=None, poderes=None, personagem=None):
        self.nome = raca
        match raca:
            case 'humano':
                personagem.atributos.adicionar_mod(raca, atributos)
                pericias_enviar = {pericias[i]: {'palavras_chaves': ['treinado']} for i in range(len(pericias))}
                personagem.pericias.adicionar_mod(pericias_enviar)
                self.poderes = poderes
                    
            case 'anao':
                atributos = {'des': -1, 'con': 2, 'sab': 1 }
                personagem.atributos.adicionar_mod(raca, atributos)
              
                poderes_raca = Poderes_Racas()
                for titulo, poder in poderes_raca.anao.items():
                    self.poderes['passivas'][titulo] = poder

    def __str__(self):
        return(f'{self.nome}')