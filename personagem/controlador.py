class Controlador:
    def __init__(self, personagem):
        self.__personagem = personagem
        
    def iniciar(self, habilidade):
        efeito = habilidade.iniciar
        
        for titulo, lista in efeito.items():
            if titulo == 'atributos-add':
                self.__personagem.atributos.adicionar_mod(habilidade.nome, lista)
            elif titulo == 'pericias-add':
                self.__personagem.pericias.adicionar_mod(lista)
            elif titulo == 'poderes-add':
                self.__personagem.poderes.adicionar(lista)
