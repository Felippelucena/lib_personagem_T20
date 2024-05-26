class Habilidades_Raca:
    def __init__(self, personagem):
        # poderes = {'Nome do Poder': {'usar': 'poder', 'palavras_chaves': ['ativa', 'passiva', 'humano']}}
        self.__personagem  = personagem
        self.lista = {
            'anao': {'Conhecimento das Rochas':{'usar': self.conhecimento_das_rochas, 'palavras_chaves':['passiva', 'anao']},
                     'Devagar e Sempre': {'usar': self.devagar_e_sempre, 'palavras_chaves':['passiva','anao']},
                     'Duro como Pedra': {'usar': self.duro_como_pedra, 'palavras_chaves':['passiva','anao']},
                     'Tradição de Heredrimm': {'usar': self.tradicao_de_heredrimm, 'palavras_chaves':['passiva','anao']}
        }}
            
    def conhecimento_das_rochas(self):
        descricao = 'Você recebe visão no escuro e +2 em testes de Percepção e Sobrevivência realizados no subterrâneo.'
        self.__personagem.palavras_chaves['conhecimento_das_rochas'] = 'Visão no escuro'
        pericias = {
            'sobrevivencia': {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']},
            'percepcao':     {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']}
            }
        if self.__personagem.localizacao == 'subterraneo' and 'conhecimento_das_rochas' not in self.__personagem.pericias.lista['sobrevivencia']['palavras_chaves']:
            self.__personagem.pericias.adicionar_mod(pericias)
            
        elif self.__personagem.localizacao != 'subterraneo' and 'conhecimento_das_rochas' in self.__personagem.pericias.lista['sobrevivencia']['palavras_chaves']:
            self.__personagem.pericias.remover_mod(pericias)   
        return descricao
    
    def devagar_e_sempre(self):
        self.__personagem.deslocamento['devagar_e_sempre'] = 6
        descricao = 'Seu deslocamento é 6m (em vez de 9m). Porém, seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'
        return descricao
    
    def duro_como_pedra(self):
        descricao = 'Você recebe +3 pontos de vida no 1º nível e +1 por nível seguinte.'
        self.__personagem.pv['mod']['duro_como_pedra'] = 3
        self.__personagem.pv['up']['duro_como_pedra'] = 1 
        return descricao
     
    def tradicao_de_heredrimm(self):
        descricao = 'Você é perito nas armas tradicionais anãs, seja por ter treinado com elas, seja por usá-las como ferramentas de ofício. Para você, todos machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.'
        return descricao    