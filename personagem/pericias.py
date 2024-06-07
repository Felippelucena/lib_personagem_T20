class Pericias:
    def __init__(self):
        # Inicializa as perícias com seus valores base
        self.lista = {
            'acrobacia':        {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': ['penalidade_armadura']},
            'adestramento':     {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'atletismo':        {'atributo': 'for', 'base': 0, 'mod': 0, 'tags': []},
            'atuacao':          {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'cavalgar':         {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': []},
            'conhecimento':     {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'cura':             {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': []},
            'diplomacia':       {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': []},
            'enganacao':        {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': []},
            'fortitude':        {'atributo': 'con', 'base': 0, 'mod': 0, 'tags': []},
            'furtividade':      {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': ['penalidade_armadura']},
            'guerra':           {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'iniciativa':       {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': []},
            'intimidacao':      {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': []},
            'intuicao':         {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': []},
            'investigacao':     {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': []},
            'jogatina':         {'atributo': 'car', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'ladinagem':        {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': ['somente_treinado', 'penalidade_armadura']},
            'luta':             {'atributo': 'for', 'base': 0, 'mod': 0, 'tags': []},
            'misticismo':       {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'nobreza':          {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'oficio':           {'atributo': 'int', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'percepcao':        {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': []},
            'pilotagem':        {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'pontaria':         {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': []},
            'reflexos':         {'atributo': 'des', 'base': 0, 'mod': 0, 'tags': []},
            'religiao':         {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': ['somente_treinado']},
            'sobrevivencia':    {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': []},
            'vontade':          {'atributo': 'sab', 'base': 0, 'mod': 0, 'tags': []}
        }


    def adicionar_mod(self, pericias):
        # pericias = {'sobrevivencia': {'mod': 2, 'tags': ['conhecimento_das_rochas']}}
        for pericia, valores in pericias.items():
            if 'atributo' in valores:
                self.lista[pericia]['atributo'] = valores['atributo']
            if 'mod' in valores:
                self.lista[pericia]['mod'] += valores['mod']
            if 'tags' in valores:
                for chave in valores['tags']:
                    if chave not in self.lista[pericia]['tags']:
                        self.lista[pericia]['tags'].append(chave)

    def remover_mod(self, pericias):
        # pericias = {'sobrevivencia': {'mod': 2, 'tags': ['conhecimento_das_rochas']}}
        for pericia, valores in pericias.items():
            if 'mod' in valores:
                self.lista[pericia]['mod'] -= valores['mod']
            if 'tags' in valores:
                for chave in valores['tags']:
                    if chave in self.lista[pericia]['tags']:
                        self.lista[pericia]['tags'].remove(chave)