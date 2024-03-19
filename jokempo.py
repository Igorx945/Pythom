import random
import jogos
def verifVenceu(escol_jogador, escol_pc,venceu):
    if escol_jogador == escol_pc:
        return('Empate')
    elif(
        (escol_jogador == "papel" and escol_pc == 'pedra') or
        (escol_jogador == "papel" and escol_pc == 'spock') or
        (escol_jogador == "pedra" and escol_pc == 'lagarto') or
        (escol_jogador == "pedra" and escol_pc == 'tesoura') or
        (escol_jogador == "tesoura" and escol_pc == 'lagarto') or
        (escol_jogador == "tesoura" and escol_pc == 'papel') or
        (escol_jogador == "spock" and escol_pc == 'pedra') or
        (escol_jogador == "spock" and escol_pc == 'tesoura') or
        (escol_jogador == "lagarto" and escol_pc == 'spock') or
        (escol_jogador == "lagarto" and escol_pc == 'papel')
        ):
        print('Você venceu')
        venceu += 1
        print(f"Você venceu {venceu} vezes")
    else:
        print("O computador venceu")
def boasVindas():
    print('Bem vindo ao jokenpo estilo Sheldon')
    print('Escolha: Pedra, papel, tesoura, lagarto, ou Spock. ')
    print ('---------------------------------------------------------------------------------------------------------------------------------')
    print('É muito simples. Olhe  tesoura corta papel, papel cobre pedra, pedra esmaga lagarto, lagarto envenena Spock, Spock esmaga tesoura, tesoura decapita lagarto, lagarto come papel, papel refuta Spock, Spock vaporiza pedra e como sempre, pedra quebra tesoura.')
    print ('---------------------------------------------------------------------------------------------------------------------------------')
    print('escolha pedra, papel, tesoura, lagarto ou spock')
def jogar():
    opc = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    boasVindas()
    while True:
        venceu = 0
        escol_jogador = input('digite a sua escolha: ').lower()
        if escol_jogador not in opc:
            print("escolha invalida escolha novamente")
            continue 
        escol_pc = random.choice(opc)
        print(f'voce escolheu {escol_jogador} e o pc escolheu {escol_pc}.')
        resultado = verifVenceu(escol_jogador, escol_pc,venceu)
        print(resultado)
        
        jogar_novamente = input('deseja perder novamente ? [s/n]').lower()
        if jogar_novamente != "s":
            break
    jogos.escolJogo()
if(__name__=="__main__"):
    jogar()