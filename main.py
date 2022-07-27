import display
import palavra
import roleta
import temas

rodada = 1
turno = 0
p_ana = 0
p_bar = 0
p_car = 0
p_atual = 0
p_novo = 0
tema = temas.sortear_Tema()
p1, p2, p3 = temas.sortear_Palavras(tema)
p, p_ = palavra.gerar_Palavras(p1, p2, p3)
r_roleta = roleta.girar_Roleta()
ativo = "ANA"
erradas = []
usadas = []
quebrar = False

#===========================================================================================================================================================
def definir_Ganhador():
    '''Ao fim de 3 rodadas é a função que com base nos pontos dos jogadores define o
    ganhador'''
    global p_car, p_bar,p_ana
    if p_car < p_bar and p_bar > p_ana:
        return 'Barbara', p_bar
    elif p_car < p_ana and p_ana > p_bar:
        return 'Ana', p_ana
    else:
        return 'Carlos!', p_car

#===========================================================================================================================================================
def atualizar_Dados():
    '''A cada rodada é necessário atualizar os dados do jogo, essa função
    reinicializa as variaveis do jogo'''
    global tema, p1, p2, p3, p, p_, r_roleta, turno, ativo, erradas, usadas
    tema = temas.sortear_Tema()
    p1, p2, p3 = temas.sortear_Palavras(tema)
    p, p_ = palavra.gerar_Palavras(p1, p2, p3)
    r_roleta = roleta.girar_Roleta()
    turno = 0
    ativo = "ANA"
    usadas = []
    erradas = []
    quebrar = False

#===========================================================================================================================================================
def show_Display():
    '''Essa função é´responsavel por printar na tela o que esta acontecendo no jogo'''
    print('\n'*50)
    global rodada, turno, p_ana, p_bar, p_car, p_atual, ativo, p, p_, r_roleta, p_novo
    display.printar_Titulo(rodada, turno, p_ana, p_bar, p_car)
    display.printar_Roleta(ativo, p_atual, r_roleta, p_novo)
    display.printar_Palavra(tema, p_, erradas)

#===========================================================================================================================================================
def digitar_letra():
    '''essa função é responsavel por solicitar uma letra do usuario e verifica a inte
    gridade da mesma, e solicita uma nova caso necessario. Caso não essa letra é
    retornada'''
    global usadas
    letra = input('Digite Uma Letra: ')
    letra = letra.upper()
    x = False
    while palavra.verificar_Caractere(letra) == False:
        letra = input('Letra invalida, digite novamente:')
        letra = letra.upper()
    while x == False:
        if letra in usadas:
            letra = input('Letra ja testada, digite novamente:')
            letra = letra.upper()
        else:
            x = True
    usadas.append(letra)
    return letra

#===========================================================================================================================================================
def letra_existe(letra):
    '''essa função é responsavel por verificar se a letra digitada pelo usuario existe
    nas palavras sortedas'''
    global p, p_
    if palavra.verificar_Letra(letra, p):
        p_ = palavra.revelar_Letra(p, p_, letra)
        return True
    else:
        erradas.append(letra)
        return False

# ===========================================================================================================================================================
def total_Vazios(p_):
    '''Verifica se o numer de espaçoes vazios é mais que 3 ou não'''
    if p_.count('_')>3:
        return False
    else:
        return True

#===========================================================================================================================================================
def Rodadas():
    '''responsavel por gerar as rodadas do jogo'''
    global rodada, tema, p, p_
    x = 0
    endRodada = False
    while x < 3 and endRodada == False:
        rodada = x + 1
        Turnos()
        x += 1
        atualizar_Dados()
    ganhador, pontos = definir_Ganhador()
    print('\n'*30)
    print('{} ganhou com {} pontos'.format(ganhador, pontos))
    print('Começando a rodada final\n')
    tema, p = temas.sorteio_Especial()
    p_ = palavra.apagar_Palavra(p)
    p_ = rodada_Final(ganhador, pontos)
    print('\n'*30)
    display.printar_RodadaFinal(ganhador, pontos, tema, p_)
    tentativa = input('Digite a palavra Final: ')
    if(tentativa.upper() == p.upper()):
        display.printar_ResultadoFinal(ganhador, pontos)
    else:
        print('Perdeu e ficou com {}'.format(pontos))
        print('A palavra era {}'.format(p))
#===========================================================================================================================================================
def tentear_Responder():
    '''função responsavel para quendo tiver menos de 4 espaçoes vazios o jogador ter
    a chance de responder as 3 palavras'''
    global p1, p2, p3
    res = input('Deseja tentar responder? Sim = (S/s)')
    res = res.upper()
    if res == 'S':
        t_p1 = input('Digite a palavra 1: ')
        t_p2 = input('Digite a palavra 2: ')
        t_p3 = input('Digite a palavra 3: ')
        if p1 == t_p1.upper() and t_p2.upper() == p2 and p3 == t_p3.upper():
            return 'Acertou', True
        else:
            return 'Errou', True
    else:
        return '', False

#===========================================================================================================================================================
def Turnos():
    '''função responsavel por coordenar os turnos das rodadas do jogo'''
    global rodada, turno, p_ana, p_bar, p_car, p_atual, ativo, p, p_, r_roleta, p_novo, quebrar
    x = 1
    endTurno = False
    while endTurno == False:
        quebrar = False
        turno += 1
        global p_atual, ativo
        if x == 1:
            p_atual = p_ana
            ativo = 'ANA'
        elif x == 2:
            p_atual = p_bar
            ativo = 'BARBARA'
        else:
            p_atual = p_car
            ativo = 'CARLOS'
            x = 0
        existe = True
        while existe == True:
            r_roleta = roleta.girar_Roleta()
            p_novo, passou = roleta.resultado_Roleta(p_atual, r_roleta)
            show_Display()
            if total_Vazios(p_) == True:
                res, ten = tentear_Responder()
                if ten and res == 'Acertou':
                    endTurno = True
                    atualizar_Pontos(x)
                    quebrar = True
                elif ten and res == 'Errou':
                    quebrar = True
                else:
                    existe = teste_Letra(passou, x)
            else:
                existe = teste_Letra(passou, x)
            if quebrar:
                break
        x += 1

def teste_Letra(passou, x):
    existe = True
    global rodada, turno, p_ana, p_bar, p_car, p_atual, ativo, p, p_, r_roleta, p_novo, quebrar
    if passou == False:
        letra = digitar_letra()
        existe = letra_existe(letra)
        if existe:
            atualizar_Pontos(x)
    else:
        atualizar_Pontos(x)
        input('Digite ENTER para continuar')
        quebrar = True
    return existe
#===========================================================================================================================================================
def atualizar_Pontos(x):
    global p_atual, p_ana, p_car, p_bar, p_novo
    p_atual = p_novo
    if x == 1:
        p_ana = p_novo
    elif x == 2:
        p_bar = p_novo
    else:
        p_car = p_novo

#===========================================================================================================================================================
def rodada_Final(pontos, ganhador):
    '''Responsavel por gerar a rodada final apos o jogador com maior pontuação vencer'''
    global usadas, erradas, p, p_, tema
    usadas = []
    erradas = []
    letras = []
    x = 0
    print('Serão solicitadas 4 consoantes e 1 vogal')
    while x < 4:
        usadas = []
        erradas = []
        print('Digite uma consoantes')
        letra = digitar_letra()
        if letra in 'AEIOU':
            x -=1
        else:
            letras.append(letra)
        x += 1
    vogal = False
    while vogal == False:
        usadas = []
        erradas = []
        print('Digite uma vogal')
        letra = digitar_letra()
        if letra in 'AEIOU':
            letras.append(letra)
            vogal = True
    p_ = palavra.palavra_Final(p, p_, letras)
    p_ = ' '.join(list(p_))
    return p_

#===========================================================================================================================================================
def main():
    '''função main do programa'''
    Rodadas()

if __name__ == "__main__":
    main()