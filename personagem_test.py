from personagem import Personagem

def test_rolar_dados():
    personagem = Personagem(nome='Thorin')
    dados_resultados = personagem.dados.rolar(4, 4)
    assert len(dados_resultados) == 4
    assert all(valor in [1,2,3,4] for valor in dados_resultados)
    dados_resultados = personagem.dados.rolar(15, 6)
    assert len(dados_resultados) == 15
    assert all(valor in [1,2,3,4,5,6] for valor in dados_resultados)

def test_atributos_aleatorio():
    personagem = Personagem(nome='Ragnar')
    personagem.atributos.definir(dados=personagem.dados)

    # Verificar se todos os atributos foram definidos
    atributos = personagem.atributos.lista
    for atributo in ['for', 'des', 'con', 'int', 'sab', 'car']:
        assert atributo in atributos
        assert 'base' in atributos[atributo]
        
        # Verificar se os valores dos atributos estão dentro do intervalo esperado (3 a 18)
        valor = atributos[atributo]['base']
        assert -2 <= valor <= 4

def test_escolher_atributos():
    personagem = Personagem(nome='Ragnar')
    
    atributos = {'for': 3, 'des': 2, 'con': 2, 'int': 2, 'sab': 0, 'car': 0}
    personagem.atributos.definir(atributos=atributos)
    
    # Verificar se todos os atributos foram definidos
    for atributo in atributos.keys():
        assert atributos[atributo] == personagem.atributos.lista[atributo]['base']
        
        # Verificar se os valores dos atributos estão dentro do intervalo esperado (3 a 18)
        valor = personagem.atributos.lista[atributo]['base']
        assert -2 <= valor <= 4