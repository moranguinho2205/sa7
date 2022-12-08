aviao = []

def escolha():
    print ("escolha uma opcao:")
    print("opcao[1] - Registrar o numero do aviao: ")
    print("opcao[2] - Registrar a quantidade de assentos disponiveis:")
    print("opcao[3] - Reservar passagem aérea:")
    print("opcao[4] - Realizar consulta de avião:")
    print("opcao[5] - Realizar consulta de passageiro:")
    print("opcao[6] - Finalizar:")
    opcao_escolhida = int (input("opcao:"))
    return opcao_escolhida

def opcao1():
    avioes = {}
    for i in range (4):
        numero = int(input("digite o numero dos avioe:\n"))
        avioes[numero] = 0
    return avioes

def opcao2(avioes):
    numeros_avioes = [chaves for chaves in avioes if avioes[chaves] == 0]
    for i in range(4):
        assentos = int(input(" digite a quantidade de assentos disponiveis: \n"))
        avioes[numeros_avioes[i]] = assentos
    return avioes



def opcao3(avioes):
    disponiveis = avioesdisponiveis()
    print(f"avioes disponiveis sao: {disponiveis}")
    numero = int(input("digite o numero do aviao:\n"))
    print(f"esse avião tem {avioes[numero]} passagem disponiveis")
    nome = input("digite o nome do passageiro:\n")
    try:
        if avioes[numero] == 0:
            print("não há reservas para esse avião")
        else:
            quantidade = int(input("quantas passagens serao reservadas:\n"))
            if avioes[numero] - quantidade >= 0:
                avioes[numero] -= quantidade
                passageiros = {nome: f"aviao numero {numero} ,tem {quantidade} de reservas"}
            else:
                print("você está tentando reservar mais aviões do que tem disponivel")
    except:
        raise KeyError("essa avião não existe")


opcao_escolhida = escolha()
while opcao_escolhida != 6:
    if opcao_escolhida == 1:
        avioes = opcao1()
        print(avioes)
        opcao_escolhida = escolha()
    elif opcao_escolhida == 2:
        avioes = opcao2(avioes)
        print(avioes)
        opcao_escolhida = escolha()
    elif opcao_escolhida == 3:





def avioesdisponiveis():
    disponiveis = []
    chaves = list(avioes)
    for i in range(len(avioes)):
        if avioes[chaves[i]] > 0:
            disponiveis.append(chaves[i])
    return disponiveis