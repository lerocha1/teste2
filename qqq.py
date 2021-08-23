import time
import random
print('\033[33m#\033[m'*12,'\033[36m ADIVINHAÇÃO \033[m','\033[33m#\033[m'*12)
print(" \033[1;30;44m BEM VINDO AO JOGO DA ADIVINHAÇÃO \033[m")
resposta = 0
while resposta == 0:
    numero_secreto = random.randrange(0, 101)
    chute = int(input(" Digite o seu número: \n"))
    if numero_secreto == chute:
        print(" \033[36m No ângulo!! Que belo chute! Você acertou!!\033[m")
        print('\033[36m Voce escolheu o numero {} que corresponde ao numero secreto {}\033[m'.format(chute, numero_secreto))
        time.sleep(2)
        break
    else:
        print("\033[32m Mandou mal meu artilheiro! Chute fora!! Você errou!!\033[m")
    if chute > numero_secreto:
        print('O seu chute foi \033[36mmaior\033[m que o número secreto!')
        print('\033[32m Voce escolheu o numero {} e o número secreto é {}\033[m'.format(chute, numero_secreto))
        time.sleep(2)
    elif chute < numero_secreto:
        print('O seu chute foi \033[36mmenor\033[m que o número secreto!')
        time.sleep(2)
        print('\033[32m Voce escolheu o numero {} e o número secreto é {}\033[m'.format(chute, numero_secreto))
    resposta = str(input(''' Deseja continuar: 
    [0] Sim
    [1] Não \n'''))
print('############################## FIM ###################################')