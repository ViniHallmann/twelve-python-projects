import random

def chute_pessoa(x):
    count = 0
    tentativa = 0
    numero_aleatório = random.randint(1, x)
    print(numero_aleatório)
    while tentativa != numero_aleatório:
        count +=1
        tentativa = int(input('Qual número voce vai chutar? '))
        if tentativa < numero_aleatório:
            print('Tente novamente. Número chutado esta baixo')
        elif tentativa > numero_aleatório:
            print('Tente novamente. Número chutado esta alto')
    print(f'Boa, você acertou o número!!! Foram {count} tentativas até descobrir')
chute_pessoa(10)

def chute_computador(x):
    count = 0
    abaixo = 1
    acima = x
    while True:
        count += 1
        chute_aleatório = random.randint(abaixo, acima)
        resp = str(input(f'Meu chute é {chute_aleatório}. Acertei o chute? (S) ou (N) ')).strip().upper()
        if resp == 'S':
            print(f'Legal!!, acertei o número!!! Foram {count} tentativas até descobrir')
            break
        feedback = str(input('Esta abaixo do numero? Escreva (B) se sim ou (C) se meu chute estiver acima do teu numero escolhido. ')).strip().upper()
        if feedback == 'B':
            abaixo = chute_aleatório + 1
        if feedback == 'C':
            acima = chute_aleatório - 1
chute_computador(10)