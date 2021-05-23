# pedra-papel-tesoura

import time
import sys
import random


import time
import sys
import random


print("\t\|_______                           _______|/")
print("\t\|___           Bem vindo(a)!           ___|/")
print("\t\|__________                     __________|/")
print("\t\|________ Ao pedra, papel, tesoura _______|/")  
print("\t (͡ ͡° ͜ つ ͡͡°)                  (͡ ͡° ͜ つ ͡͡°)    ")
time.sleep(1)

print("...loading [■■■■■■■□] 60%")
time.sleep(1)
print("...loading [■■■■■■■■□] 67%")
time.sleep(1)
print("...loading [■■■■■■■■■□] 81%")
time.sleep(1)
print("...loading [■■■■■■■■■] 97%")
time.sleep(1.6)
print("→_→...loading [■■■■■■■■■] 99%")
time.sleep(0.6)


def ganhou():
    print("Máquina: Tu ganhaste, queres uma medalha?")

def perdeu():
    print("Máquina: Tu perdeste...ganda BOT")

def Empate():
    print ("Máquina: Empate")


def O_Jogo():

    moves = ['pedra', 'papel', 'tesoura']

    print('O Jogo: pedra, papel, tesoura?')
    tentativas = 3
    while True:
        if tentativas == 0:
            print('Máquina: Acabaram se as tuas tentativas.... Xau.')
            time.sleep(3)
            sys.exit(0)
        Jogador = str(input('Jogador: ')).lower()
        if Jogador.lower() not in moves:
            print(f'Máquina: Opçôes inválidas! tu tens ainda {tentativas} tentativas.')
            tentativas -= 1
        else:
            máquina = random.choice(moves)
            print(f'máquina: {máquina}')

            if Jogador == máquina:
                Empate()
            elif Jogador == 'Pedra' and máquina == 'tesoura':
                ganhou()
            elif Jogador == 'pedra' and máquina == 'papel':
                perdeu()
            elif Jogador == 'papel' and máquina  == 'pedra':
                ganhou()
            elif Jogador == 'papel' and máquina == 'tesoura':
                perdeu()
            elif Jogador == 'tesoura' and máquina == 'papel':
                ganhou()
            elif Jogador == 'tesoura' and máquina == 'pedra':
                perdeu()
            else:
                pass

            play_again = str(input('Máquina: Queres Jogar outra? (s/n): '))
            if play_again.lower() == 's':
                O_Jogo()
            elif play_again.lower() == 'n':
                print('Máquina: Game Over. Xau.')
                time.sleep(2.5)
                sys.exit(0)
            else:
                print('Máquina: Opções inválidas. Xau...')
                time.sleep(2.5)
                sys.exit(0)


if __name__=='__main__':
    O_Jogo()
