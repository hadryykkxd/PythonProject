# Importa o módulo random para gerar números aleatórios
import random


# Define a função principal do jogo chamada 'jogo_adivinhacao'
def jogo_adivinhacao():
    # Exibe mensagem de boas-vindas ao jogador
    print("Bem-vindo ao Jogo de Adivinhação!")

    # Gera um número aleatório entre 1 e 10 que o jogador precisa adivinhar
    numero_secreto = random.randint(1, 10)

    # Inicializa o contador de tentativas com 0
    tentativas = 0

    # Loop infinito (só termina quando o jogador acertar)
    while True:
        # Solicita ao jogador um palpite e converte para inteiro
        palpite = int(input("Adivinhe o número (1 a 10): "))

        # Incrementa o contador de tentativas a cada palpite
        tentativas += 1

        # Verifica se o palpite está correto
        if palpite == numero_secreto:
            # Mensagem de parabéns mostrando quantas tentativas foram necessárias
            print(f"Parabéns! Acertou em {tentativas} tentativas!")
            break  # Encerra o loop do jogo

        # Se o palpite for menor que o número secreto
        elif palpite < numero_secreto:
            print("Tente um número maior!")  # Dica para o jogador

        # Se o palpite for maior que o número secreto
        else:
            print("Tente um número menor!")  # Dica para o jogador


# Chama a função para iniciar o jogo
jogo_adivinhacao()