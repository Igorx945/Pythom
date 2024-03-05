import forca
import adivinhacao

def escolaJogo():
    print("escolha o jogo")
    print("1- forca")
    print("2- adivinhacao")
    escolha = int(input("digite a opcao"))
    if escolha == 1:
        forca.jogarForca()
    elif escolha == 2:
        adivinhacao.jogarAdvinha()
    else:
        print("digite 1 ou 2 baiano")
escolaJogo()