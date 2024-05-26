from .habilidades_raca import Habilidades_Raca

class Raca:
    def __init__(self, personagem):
        self.nome = None
        self.__personagem = personagem
        
    def definir(self,raca, atributos=None, pericias=None, poderes=None):
        self.nome = raca
        habilidades_raca = Habilidades_Raca(self.__personagem)
        match raca:
            case 'humano':
                self.__personagem.atributos.adicionar_mod(raca, atributos)
                pericias_enviar = {pericias[i]: {'palavras_chaves': ['treinado', raca]} for i in range(len(pericias))}
                self.__personagem.pericias.adicionar_mod(pericias_enviar)
                self.__personagem.poderes.adicionar(poderes) if len(pericias) == 1 else ''
                    
            case 'anao':
                atributos = {'des': -1, 'con': 2, 'sab': 1 }
                self.__personagem.atributos.adicionar_mod(raca, atributos) 
                self.__personagem.poderes.adicionar(habilidades_raca.lista[raca])

            case 'dahllan':
                pass
            
            case 'elfo':
                pass
            
            case 'goblin':
                pass
            
            case 'lefou':
                pass
            
            case 'minotauro':
                pass
            
            case 'qareen':
                pass
            
            case 'golem':
                pass
            
            case 'hynne':
                pass
            
            case 'kliren':
                pass
            
            case 'medusa':
                pass
            
            case 'osteon':
                pass
            
            case 'seria/tritao':
                pass
            
            case 'silfide':
                pass
            
            case 'suraggel':
                pass
            
            case 'trog':
                pass
            
    def __str__(self):
        return(f'{self.nome}')