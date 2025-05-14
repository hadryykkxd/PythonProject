# Importa o módulo random para escolhas aleatórias do computador
import random


# Define a função principal do jogo
def jogo_pedra_papel_tesoura():
    # Lista com as opções válidas do jogo
    opcoes = ["pedra", "papel", "tesoura"]

    # Mensagem de boas-vindas
    print("Bem-vindo ao Pedra, Papel, Tesoura!")

    # Loop infinito (só termina quando jogador digitar 'sair')
    while True:
        # Solicita a escolha do jogador e converte para minúsculas
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para parar): ").lower()

        # Verifica se o jogador quer sair do jogo
        if jogador == "sair":
            break  # Sai do loop while

        # Valida se a escolha do jogador é uma opção válida
        if jogador not in opcoes:
            print("Escolha inválida!")
            continue  # Volta para o início do loop

        # Computador escolhe aleatoriamente uma das opções
        computador = random.choice(opcoes)

        # Mostra a escolha do computador
        print(f"Computador escolheu: {computador}")

        # Verifica condições de empate
        if jogador == computador:
            print("Empate!")

        # Verifica todas as condições de vitória do jogador:
        # Pedra ganha da tesoura, papel ganha da pedra, tesoura ganha do papel
        elif (jogador == "pedra" and computador == "tesoura") or \
                (jogador == "papel" and computador == "pedra") or \
                (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")

        # Se não for empate e jogador não venceu, então computador vence
        else:
            print("Computador venceu!")


# Chama a função para iniciar o jogo
jogo_pedra_papel_tesoura()