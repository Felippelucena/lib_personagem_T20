from .atributos import Atributos
from .raca import Raca
from .pericias import Pericias
from .dados import Dados
from .poderes import Poderes

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.dados = Dados()
        self.atributos = Atributos()
        self.raca = Raca()
        self.poderes = Poderes()
        self.classe = None
        self.origem = None
        self.divindade = None
        self.pericias = Pericias()
        self.pv = { 'atual': 10, 'up': {'base':2}, 'mod': {}}
        self.pm = { 'atual': 5, 'up': {'base':1}, 'mod': {}}
        self.localizacao = None
        self.palavras_chaves = {}
        self.deslocamento = {'base': 9}
        
    def pv_max(self):
        pv = 10 + self.atributos.total()['con'] + self.nivel + sum(self.pv['mod'].values())
        return pv
    
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Raça: {self.raca}\n"
            f"Classe: {self.classe}\n"
            f"Nível: {self.nivel}\n"
            f"Divindade: {self.divindade}\n"
            f"Atributos: {self.atributos}\n"
            f"PV Atual: {self.pv['atual']}\n"
            f"PV Máximo: {self.pv_max()}\n"
            f"PM Atual: {self.pm['atual']}\n"
            f"Localização: {self.localizacao}\n"
        )

    def passivas(self):
        for valores in self.poderes.lista.values():
            valores['usar']() if 'passiva' in valores['palavras_chaves'] else ''
        
        for valores in self.raca.habilidades.values():
            valores['usar']() if 'passiva' in valores['palavras_chaves'] else ''