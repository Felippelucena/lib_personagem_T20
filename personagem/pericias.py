class Pericias:
    def __init__(self):
        # Inicializa as perícias com seus valores base
        self.lista = {
            'acrobacia':        {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': ['penalidade_armadura']},
            'adestramento':     {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'atletismo':        {'atributo': 'for', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'atuacao':          {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'cavalgar':         {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'conhecimento':     {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'cura':             {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'diplomacia':       {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'enganacao':        {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'fortitude':        {'atributo': 'con', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'furtividade':      {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': ['penalidade_armadura']},
            'guerra':           {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'iniciativa':       {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'intimidacao':      {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'intuicao':         {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'investigacao':     {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'jogatina':         {'atributo': 'car', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'ladinagem':        {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado', 'penalidade_armadura']},
            'luta':             {'atributo': 'for', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'misticismo':       {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'nobreza':          {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'oficio':           {'atributo': 'int', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'percepcao':        {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'pilotagem':        {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'pontaria':         {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'reflexos':         {'atributo': 'des', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'religiao':         {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': ['somente_treinado']},
            'sobrevivencia':    {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': []},
            'vontade':          {'atributo': 'sab', 'base': 0, 'mod': 0, 'palavras_chaves': []}
        }


    def adicionar_mod(self, pericias):
        # pericias = {'sobrevivencia': {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']}}
        for pericia, valores in pericias.items():
            if 'atributo' in valores:
                self.lista[pericia]['atributo'] = valores['atributo']
            if 'mod' in valores:
                self.lista[pericia]['mod'] += valores['mod']
            if 'palavras_chaves' in valores:
                for chave in valores['palavras_chaves']:
                    if chave not in self.lista[pericia]['palavras_chaves']:
                        self.lista[pericia]['palavras_chaves'].append(chave)

    def remover_mod(self, pericias):
        # pericias = {'sobrevivencia': {'mod': 2, 'palavras_chaves': ['conhecimento_das_rochas']}}
        for pericia, valores in pericias.items():
            if 'mod' in valores:
                self.lista[pericia]['mod'] -= valores['mod']
            if 'palavras_chaves' in valores:
                for chave in valores['palavras_chaves']:
                    if chave in self.lista[pericia]['palavras_chaves']:
                        self.lista[pericia]['palavras_chaves'].remove(chave)