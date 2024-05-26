class Poderes_Racas:
    def __init__(self):
        self.anao = {'Conhecimento das Rochas':self.conhecimento_das_rochas,
                     'Devagar e Sempre': self.devagar_e_sempre,
                     'Duro como Pedra': self.duro_como_pedra,
                     'Tradição de Heredrimm': self.tradicao_de_heredrimm}
        
            
    def conhecimento_das_rochas(self, personagem):
        descricao = 'Você recebe visão no escuro e +2 em testes de Percepção e Sobrevivência realizados no subterrâneo.'
        personagem.palavras_chaves['conhecimento_das_rochas'] = 'Visão no escuro'
        pericias = {
            'sobrevivencia': {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']},
            'percepcao':     {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']}
            }
        if personagem.localizacao == 'subterraneo' and 'conhecimento_das_rochas' not in personagem.pericias.lista['sobrevivencia']['palavras_chaves']:
            personagem.pericias.adicionar_mod(pericias)
            
        elif personagem.localizacao != 'subterraneo' and 'conhecimento_das_rochas' in personagem.pericias.lista['sobrevivencia']['palavras_chaves']:
            personagem.pericias.remover_mod(pericias)
            
        return descricao
    
    def devagar_e_sempre(self, personagem):
        personagem.deslocamento['devagar_e_sempre'] = 6
        descricao = 'Seu deslocamento é 6m (em vez de 9m). Porém, seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'
        return descricao
    
    def duro_como_pedra(self, personagem):
        descricao = 'Você recebe +3 pontos de vida no 1º nível e +1 por nível seguinte.'
        personagem.pv['mod']['duro_como_pedra'] = 3
        personagem.pv['up']['duro_como_pedra'] = 1 
        return descricao
     
    def tradicao_de_heredrimm(self, personagem):
        descricao = 'Você é perito nas armas tradicionais anãs, seja por ter treinado com elas, seja por usá-las como ferramentas de ofício. Para você, todos machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.'
        return descricao    