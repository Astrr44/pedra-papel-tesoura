# pedra-papel-tesoura

import time
import sys
import random


def win():
    print('O Jogo: Tu ganhaste, queres uma medalha?')

def lost():
    print('O Jogo: Tu perdeste...ganda BOT')

def draw():
    print('O Jogo: Empate.')


def O_Jogo():

    moves = ['pedra', 'papel', 'tesoura']

    print('O Jogo: pedra, papel, tesoura?')
    tentativas = 3
    while True:
        if tentativas == 0:
            print('O Jogo: Acabaram se as tuas tentativas. Xauuuu.')
            time.sleep(4)
            sys.exit(0)

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f'O Jogo: Opçôes inválidas! tu tens ainda {tentativas} tentativas.')
            tentativas -= 1
        else:
            máquina = random.choice(moves)
            print(f'máquina: {máquina}')

            if player == máquina:
                draw()
            elif player == 'Pedra' and máquina == 'tesoura':
                win()
            elif player == 'pedra' and máquina == 'papel':
                lost()
            elif player == 'papel' and máquina  == 'pedra':
                win()
            elif player == 'papel' and máquina == 'tesoura':
                lost()
            elif player == 'tesoura' and máquina == 'papel':
                win()
            elif player == 'tesoura' and máquina == 'pedra':
                lost()
            else:
                pass

            play_again = str(input('O Jogo: Queres tentar outraves? (s/n): '))
            if play_again.lower() == 's':
                O_Jogo()
            elif play_again.lower() == 'n':
                print('O Jogo: Game Over. Xau.')
                time.sleep(2.5)
                sys.exit(0)
            else:
                print('O Jogo: Opções inválidas. Xau...')
                time.sleep(2.5)
                sys.exit(0)


if __name__=='__main__':
    O_Jogo()
