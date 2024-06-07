class Habilidade:
    def __init__(self, nome, descricao, passiva=None, ativa=None, iniciar = None):
        self.nome = nome
        self.descricao = descricao
        self.passiva = passiva
        self.ativa = ativa
        self.iniciar = iniciar

    def __str__(self):
        return f'{self.nome} ({self.descricao}) - Ativa: {self.ativa} - Passiva: {self.passiva}'