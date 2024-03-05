import random
tentativas = 0
max_tentativas = 6
numSecreto = random.randint(0,12)
def jogarAdvinha():
    while tentativas < max_tentativas:
        palpite = int(input('Digite seu palpite'))
        tentativas += 1
    
        if palpite == numSecreto:
            print(f'Parabens vc acertou em {tentativas} tentativas')
            break
        elif palpite < numSecreto:
            print ('Quase la, e um numero maior')
        else:
            print('Quase la, e um numero menor')
        
        if tentativas == max_tentativas:
            print ('vc esgotou o numero de tentativas')
            break
        else:
            print(f'Vc tem ainda {max_tentativas - tentativas} tentativas')
    print('Fim de jogo')
if(__name__=="__main__"):
     jogarAdvinha()