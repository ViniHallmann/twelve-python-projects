
import string
import random
def listaPalavra():
    lista_de_palavras = 'Aviao Elefante Bola Bebe Peixe Futebol Beliscao Basquete Controle Triste Gato Golfe Tesoura Colher Pular Galinha Sapo Espirro Martelo Violao Aplaudir Tosse Chifres Pinguim Chorar Rabo Piada Escova  Celular Cachorro Pato Sofa Fotografo oculos  Bale Pipa Cafe Taxi Cadeira onibus Elevador Bicicleta Fogao Copo Orelhas Chocolate Pescador Notebook Lapis'
    palavra_separadas = list()
    palavra = list()
    for palavra in lista_de_palavras.split():
        palavra_separadas.append(palavra) 
    return palavra_separadas

def palavraEscolhida():
    numeroAleatório = random.randint(0,48)
    pEscolhida = listaPalavra()[numeroAleatório]
    return pEscolhida

def jogoForca():
    palavra = palavraEscolhida().upper()
    letrasPalavra = set(palavra) 
    letrasUsadas = set()
    tentativas = 7
    alfabeto = set(string.ascii_uppercase)

    print(palavra)
    while len(letrasPalavra) >  0 and tentativas > 0:
        #letras chutadas
        print(f'Voce tem {tentativas} tentativas e ja usou essas letras: ', ' '.join(letrasUsadas))
        
        #mostra as letras chutadas que estao corretas
        letrasChutadasCerta = []
        for letra in palavra:
            if letra in letrasUsadas:
                letrasChutadasCerta += letra
            else: 
                letrasChutadasCerta += '_'

        for v in letrasChutadasCerta:
            print(f'{v}',end ='')
        #o usuário chuta uma letra
        chute = str(input('\nChute uma letra: ')).upper()
        if chute == 'SAIR':
            break
        if chute in alfabeto - letrasUsadas:# adiciona o chute nas letrasUsadas
            letrasUsadas.add(chute)
            if chute in letrasPalavra: # se a letra esta nas letras da Palavra, remove o chute do set letrasPalavra
                letrasPalavra.remove(chute)
            else:
                tentativas -= 1
                print('Essa letra nao esta na palavra\n')
        elif chute in letrasUsadas: # se o chute for igual a uma letrasUsadas dentro do set, retorna um erro.
            print('Voce ja usou essa letra!. Tente novamente\n')
            
    if tentativas == 0:
        print(f'Voce morreu..., a palavra era {palavra}')
    else: 
        print(f'Voce acertou!!! A palavra era {palavra}')
            
jogoForca()




