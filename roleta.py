import random
def gerar_Roleta():
    '''Cria uma lista contendo a roleta, com os pontos de 10 - 1000, perdeu tudo e passou a vez'''
    lista_pontos = list(range(100, 950, 50))
    lista_roleta = ['Perdeu tudo', 'Perdeu tudo', '1000', '1000', 'Passou a vez', 'Passou a vez']
    for ponto in lista_pontos:
        lista_roleta.append(ponto)
    return lista_roleta

#===========================================================================================================================================================
def girar_Roleta():
    '''gera a roleta e obtem um item random da mesma'''
    resultado = random.choice(gerar_Roleta())
    return str(resultado)

#===========================================================================================================================================================
def resultado_Roleta(p_atual, r_roleta):
    '''recebe a pontuação do jogador atual e o resultado da roleta, retorna o valor
    final da pontuação do jogador'''
    p_final = 0
    passou = False
    if r_roleta == 'Perdeu tudo':
        p_final = 0
        passou = True
    elif r_roleta == 'Passou a vez':
        p_final = p_atual
        passou = True
    else:
        p_final = p_atual + int(r_roleta)
    return p_final, passou