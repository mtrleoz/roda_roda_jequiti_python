import random
baseDados = {'Cor':['azul', 'amarelo', 'preto', 'verde'],
             'Pais':['brasil', 'Mexico', 'Argentina', 'Paraguai'],
             'Frutas':['Maca', 'Abacaxi', 'Pera', 'Uva']}

def sortear_Tema():
    '''Sorteia uma chave aleatorio do dicionario baseDados'''
    chaves = list(baseDados.keys())
    resultado = random.choice(chaves)
    return resultado

#===========================================================================================================================================================
def sortear_Palavras(tema):
    '''dado o tema sorteado é retornado 3 palavra desse tema escolhidas aleatoriamente'''
    palavras = list(baseDados.get(tema))
    p1 = random.choice(palavras)
    palavras.remove(p1)
    p2 = random.choice(palavras)
    palavras.remove(p2)
    p3 = random.choice(palavras)
    palavras.remove(p3)
    return p1.upper(), p2.upper(), p3.upper()

#===========================================================================================================================================================
def sorteio_Especial():
    '''Realiza o sorteio da rodada final do jogo'''
    tema = sortear_Tema()
    palavras = list(baseDados.get(tema))
    palavra = random.choice(palavras)
    return tema, palavra


