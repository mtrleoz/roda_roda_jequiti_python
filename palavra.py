def gerar_Palavras(p1, p2, p3):
    '''dado as 3 palavras sorteadas retorna uma string para as palavras concatenadas e
    separadas por '/' e a mesma string só que as letras subistitudas por '_' '''
    p_ = apagar_Palavra(p1)+'/'+apagar_Palavra(p2)+'/'+apagar_Palavra(p3)
    p = p1 + '/' + p2 + '/' + p3
    p = ' '.join(list(p))
    p_ = ' '.join(list(p_))
    return p, p_

#===========================================================================================================================================================
def apagar_Palavra(palavra):
    '''dado uma string substitui as letras por '_' '''
    p_ = ''
    for x in list(palavra):
        p_ += '_'
    return p_

#===========================================================================================================================================================
def verificar_Letra(letra, p):
    '''Verifica a existencia da letra digirada pel o jogador nas palavras sorteadas'''
    if letra in p.upper():
        return True
    else:
        return False

#===========================================================================================================================================================
def revelar_Letra(p, p_, letra):
    '''dado a string com as 3 palavras, a string respectiva com palavras escondidas e a letra
    caso a letra esteja nas palavras é retornado a string com a letra em questão revelada'''
    lst_p_ = list(p_)
    for x in range(p.count(letra)):
        lst_p_[p.index(letra)] = letra.upper()
        p = p.replace(letra,'*', 1)
    return ''.join(lst_p_)

#===========================================================================================================================================================
def verificar_Caractere(letra):
    '''verifica se a letra digitada esta entre os caracteres do alfabeto padrão'''
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(letra) != 1:
        return False
    elif letra.upper() in letras:
        return True
    else:
        return False
#===========================================================================================================================================================
def palavra_Final(p, p_, letras):
    '''revela as letras escolhidas para a palavra da rodada final'''
    for letra in letras:
        p_ = revelar_Letra(p.upper(), p_, letra.upper())
        print(p_)
    return p_

