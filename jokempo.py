import random

def jogarJk():
    opcoes = ["pedra", "papel", "tesoura"]
    print("Bem vindo ao jogo")
    print("Escola: pedra, papel ou tesoura.")
    
    while True:
        escolhaJg = input("sua escolha:").lower()
        if escolhaJg not in opcoes:
            print("escolha errada.Tente novamente")
            continue

        escolhaComp = random.choice(opcoes)
        print(f"Compudor escolheu: {escolhaComp}")

        if escolhaJg == escolhaComp:
            print("Empate")
        elif(
            (escolhaJg == "papel" and escolhaComp == "pedra") or
            (escolhaJg == "pedra" and escolhaComp == "tesoura") or
            (escolhaJg == "tesoura" and escolhaComp == "papel")
            ):
            print("Vc ganhou")
        else:
            print("vc perdeu")

        jogarDnv = input("vc quer jogar novamente?").lower()
        if jogarDnv != "sim":
            break

if(__name__=="__main__"):
    jogarJk()


