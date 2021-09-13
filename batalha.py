from time import sleep
from random import randint

vida_player = 50
vida_inimigo = 50

jogo = input('Quer jogar? [S]im [N]ao   ').lower()

if jogo == 's':
    print('\n\nEsse jogo será uma lutinha.\nSeu objetivo é fazer o inimigo ficar com 0 de vida.')

    while True:
        des = int(input('''\n\nSua vez!!!\nEscolha sua jogada: 
[1] Atacar
[2] Curar'''))

        if vida_player >= 50 and des == 2:
            while True:
                print('Vida cheia... Faça outra escolha: ')
                des = int(input('''[1] Atacar
[2] Curar'''))
                if des == 1:
                    break

        if vida_player != 50 or vida_inimigo != 500:
            print(f'\nSua vida é: {vida_player}\nA vida do inimigo é: {vida_inimigo}\n')

        if des == 1:
            print('\nVocê decidiu atacar!')
            print('Calculando dano...\n')
            danop = randint(0, 10)
            sleep(2)
            vida_inimigo -= danop
            if danop > 0:
                print(f'Você deu um total de {danop} de dano!')
            if danop == 0:
                print('O inimido desviou...')

        if vida_inimigo == 0:
            print('\nVocê venceu!!!\nParabéns!!!')
            break

        elif des == 2:
            print('\nVocê decidiu se curar!')
            print('Curando...')
            sleep(2)
            cura = randint(5, 10)
            vida_player += cura
            print(f'\nVocê curou {cura} de vida!')

        print('\nVez do inimigo...')
        escini = randint(1, 2)

        if vida_inimigo >= 50 and escini == 2:
            while True:
                escini = randint(1)
                break

        if escini == 1:
            print('\nO inimigo decidiu atacar!')
            danoi = randint(0, 10)
            print('Calculando dano...\n')
            vida_player -= danoi
            sleep(2)
            if danoi > 0:
                print(f'O inimigo deu {danoi} de dano!')
            if danoi == 0:
                print('Você desviou...')

        if vida_player == 0:
            print('\nVocê perdeu!\nQue pena')
            break

        elif escini == 2:
            print('\nO inimigo decidiu se curar!')
            print('Curando...')
            curaini = randint(5, 10)
            vida_inimigo += curaini
            sleep(2)
            print(f'\nO inimigo curou {curaini} de vida!')


elif jogo == 'n':
    print('É uma pena...\n Mas é sua escolha.')

elif jogo != 's' 'n':
    while True:
        print('Informação inválida!\nDigite novamente:')
        jogo = input('[S]im [N]ao   ').lower()
        if jogo == 's' or jogo == 'n':
            break
