def mostra_linha():
    """
    Mostra uma linha de separação.
    """
    print('-' * 50)

# Exemplo de uso da função mostra_linha
mostra_linha()

print("Aluguel de Carros com a maior frota do Brasil | Localiza")

mostra_linha()

print("Seja Bem vindo!")

# Exemplo de uso da função mostra_linha
mostra_linha()

nome = input("Digite seu nome: ")

print(f"Olá, {nome}! Estamos felizes em tê-lo conosco.")

mostra_linha()

print("Selecione o carro que deseja alugar:")

def mostra_opcoes():
    """
    Mostra as opções de carros disponíveis para aluguel.
    """
    print("1 - BMW")
    print("2 - MUSTANG")
    print("3 - HB20")
    print("4 - FUSCA")
    print("5 - CIVIC")
    print("0 - SAIR")

mostra_opcoes()

mostra_linha()

carro_escolhido = input("Digite o número do carro escolhido: ")

match carro_escolhido:
    case '1':
        print("Você escolheu o carro: BMW , valor do dia: R$ 500,00")
    case '2':
        print("Você escolheu o carro: MUSTANG , valor do dia: R$ 2000,00")
    case '3':
        print("Você escolheu o carro: HB20, valor do dia: R$ 130,00")
    case '4':
        print("Você escolheu o carro: FUSCA, valor do dia: R$ 250,00")
    case '5':
        print("Você escolheu o carro: CIVIC, valor do dia: R$ 180,00")
    case '0':
        print("Saindo do programa...")
        exit()  # Encerra o programa se o código for 0
    case _:
        print("Código inválido. Por favor, selecione um código do menu.")

mostra_linha()

