from .habilidades_raca import Habilidades_Raca

class Construtor:
    def __init__(self, personagem):
        self.__personagem = personagem
    
    def definir_atributos(self, dados=None, atributos=None):
        
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
            for atributo, valor in zip(self.__personagem.atributos.lista.keys(), resultados):
                self.__personagem.atributos.lista[atributo]['base'] = valor 
            self.__personagem.atributos.pontos = 0 
                           
        else:
            #ESCOLHER
            custo = { -1: 1, 0: 0, 1: -1, 2: -2, 3: -4, 4: -7 }
            if self.__personagem.atributos.pontos == 10:
                self.__personagem.atributos.pontos += sum(custo[atributo] for atributo in atributos.values())
                
                if self.__personagem.atributos.pontos == 0:
                    for atributo, valor in atributos.items():
                        self.__personagem.atributos.lista[atributo]['base'] = valor
                else:
                    self.__personagem.atributos.pontos = 10
                    
        self.__personagem.poderes.adicionar({'Atributos Mínimos': {'usar': self.__personagem.atributos.atributos_minimos, 'palavras_chaves': ['passiva', 'atributos']}})
        
    def definir_raca(self,raca, atributos=None, pericias=None, poderes=None):
        
        self.__personagem.raca.nome = raca
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
                self.__personagem.raca.adicionar_habilidade(habilidades_raca.lista[raca])

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
            