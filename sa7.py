aviao = []
passageiros = {}
def avioesdisponiveis():
    disponiveis = []
    chaves = list(avioes)
    for i in range(len(avioes)):
        if avioes[chaves[i]] > 0:
            disponiveis.append(chaves[i])
    return disponiveis
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
        numero = int(input("digite o numero dos aviões:\n"))
        avioes[numero] = 0
    return avioes

def opcao2(avioes):
    numeros_avioes = [chaves for chaves in avioes if avioes[chaves] == 0]
    for i in range(4):
        assentos = int(input(" digite a quantidade de assentos disponiveis: \n"))
        avioes[numeros_avioes[i]] = assentos
    return avioes



def opcao3(avioes):
    print(f"avioes disponiveis sao: {avioesdisponiveis()}")
    numero = int(input("digite o numero do aviao:\n"))
    print(f"esse avião tem {avioes[numero]} passagem disponiveis")
    nome = input("digite o nome do passageiro:\n")
    try:
        if avioes[numero] == 0:
            print("não há reservas para esse avião")
        else:
            quantidade = int(input("quantas passagens serao reservadas:\n"))
            if nome not in passageiros:
                passageiros[nome] = 0
            if avioes[numero] - quantidade >= 0:
                avioes[numero] -= quantidade
                passageiros[nome] += quantidade
            else:
                print("você está tentando reservar mais aviões do que tem disponivel")
    except:
        raise KeyError("essa avião não existe")

def opcao4():
    print(f"avioes disponiveis sao: {avioesdisponiveis()}")
    numero = int(input("digite o numero do aviao:\n"))
    print(f"esse avião tem {avioes[numero]} passagem disponiveis")

def opcao5():
    nome = input("digite o nome do passageiro:\n")
    print(f"esse passageiro tem {passageiros[nome]} passagem reservadas")


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
        opcao3(avioes)
        opcao_escolhida = escolha()
    elif opcao_escolhida == 4:
        opcao4()
        opcao_escolhida = escolha()
    elif opcao_escolhida == 5:
        opcao5()
        opcao_escolhida = escolha()
print("fechando o programa")



