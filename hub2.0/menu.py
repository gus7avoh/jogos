import smart

def menuPrincipal():
    smart.limpar_terminal()
    print("-="*79)
    print("LISTA DE JOGOS".center(140))
    print("\n1 - Pedra papel e tesoura ")
    print("2 - jogo da forca ")
    print("3 - Par ou impar ")
    print("4 - Adivinhe um numero ")

    while True:
        p = int(input("\n\033[1;34mDigite o numero referente ao jogo que deseja jogar: \033[m"))
        if p in [1, 2, 3, 4]:
            break
        else:
            print("\n\033[1;31mOpçao invalida! \033[m")
    return p


def cabeçalho(txt):
        texto = str(txt).upper()
        print("\033[1;35m-=\033[m"*79)
        print(f"{texto}".center(140))
        print("\033[1;35m-=\033[m"*79)





