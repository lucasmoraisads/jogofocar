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
        continue
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
    
    if erros >= 1:
        print("X  O  ")
    else:
        print('X')    
        
    linha2 = ''
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " /| "
    elif erros >= 4:
        linha2 = " /|\  "
        print(f'X{linha2}')
        
    linhas3 = ""
    if erros == 5:
        linhas3 += " / "
    elif erros >=6:
        linhas3 += " / \  "
    print(f'X{linhas3}')
    print(f'X\n========')
    
    
    # condição de fim de  jogo
    
    if erros ==6:
        print('Enforcado')
        print(f'A palavra correta era {palavra}')
        break