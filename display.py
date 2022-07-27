titulo   = '1'
palavra  = '2'
roleta   = '3'

def printar_Titulo(rodada, turno, p_ana, p_bar, p_carlos):
    '''Exibe a parte do titulo do display'''
    titulo = "+================================================\n"
    titulo += '| RODADA ' + str(rodada) + ' - TURNO ' + str(turno) +'\n'
    titulo += "+================================================\n"
    titulo += '| ANA - ' + str(p_ana) + ' | BARBARA - ' + str(p_bar) + ' | CARLOS - ' + str(p_carlos)+'\n'
    titulo += "+================================================\n"
    print(titulo)

#===========================================================================================================================================================
def printar_Roleta(ativo, p_atual, r_roleta, p_nova):
    '''exibe a parte com as informaçoes da roleta e da rodada atual'''
    roleta = 'Jogador ativo: <' + ativo+'>\n'
    roleta += 'Pontuação atual: <' + str(p_atual) +'>\n'
    roleta += 'Roleta: <' + r_roleta + '>\n'
    roleta += 'Nova Pontuação: <' + str(p_nova) + '>\n'
    print(roleta)

#===========================================================================================================================================================
def printar_Palavra(tema, p_, erradas):
    '''exibe as palavras do jogo escondidas'''
    palavras = p_.split('/')
    palavra = "+================================================\n"
    palavra += 'Tema: <' + tema + '>\n'
    palavra += 'P1) ' + palavras[0] + '\n'
    palavra += 'P2)' + palavras[1] + '\n'
    palavra += 'P3)' + palavras[2] + '\n'
    l_errada = ''
    for letra in erradas:
        l_errada += letra + ', '
    palavra += 'Letras erradas: <' + l_errada + '> \n'
    palavra += "+================================================\n"
    print(palavra)
#===========================================================================================================================================================

def printar_RodadaFinal(atual, p_atual, tema, p_):
    '''exibe as informações da rodada final do jogo'''
    titulo = "+================================================\n"
    titulo += '| RODADA FINAL\n'
    titulo += "+================================================\n"
    titulo += '|' + str(atual) + ': ' + str(p_atual)+'\n'
    titulo += "+================================================\n"
    print(titulo)
    print('Pontuação atual: <' + str(p_atual)+'>\n')
    print('Nova Pontuação: <' + str(p_atual*2) + '>\n')
    print("+================================================\n")
    print('Tema: <'+ tema +'>\n')
    print('Palavra: <' + p_ + '>\n')

#===========================================================================================================================================================
def printar_ResultadoFinal(atual, pontos):
    '''exive o resultado final do jogo'''
    print('\n'*30)
    print("+================================================\n")
    print('{} ganhou com {} pontos'.format(atual, pontos*2))



