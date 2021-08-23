def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["", "", "", "", "", ""]


    enforcou = False
    acertou = False
    erros = 0


    #teste git

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual Letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
               if (chute == letra):
                   letras_acertadas[index] = letra
               index +=1
        else:
            erros += 1

        enforcou = erros ==6

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()