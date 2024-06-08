palavra = input('Digite uma palavra secreta: ').lower().strip()

for x in range(50):
    print()
    
digitadas = []
acertos   = []
erros     = 0

while True:
    adivinha = ""
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '\u2588'
    print(f'ADIVINHA ({len(palavra)} letras):')
    for letra in adivinha:
        print(f'{letra} ', end='')
        
    print()
    # condição de vitoria
    if adivinha == palavra:
        print('Você acertou!')
        break
    
    # tentativas
    
    tentativas = input('\nDigite uma letra:').lower().strip()
    if tentativas in digitadas:
        print('Você ja usou essa letra!')
        continue\
    else:
        digitadas += tentativas
        if tentativas in palavra:
            acertos += tentativas
        else:
            erros += 1
            print('Você errou!')
    #desenhando a forcar      
    print("X==:==")
    print("x  :  ")
    