# Importa o módulo random que será usado para gerar números aleatórios
import random


# Define a função principal do jogo chamada 'jogo_aventura'
def jogo_aventura():
    # Exibe mensagem de boas-vindas ao jogador
    print("Bem-vindo à Aventura na Floresta!")
    # Exibe a situação inicial do jogo
    print("Você está numa floresta. Escolha seu caminho.")

    # Inicializa a variável vida com valor 3 (o jogador começa com 3 vidas)
    vida = 3

    # Loop principal do jogo que continua enquanto o jogador tiver vidas restantes
    while vida > 0:
        # Exibe a quantidade de vidas atual do jogador
        print(f"Vida: {vida}")

        # Solicita ao jogador que faça uma escolha de caminho
        escolha = input("Digite 1 (ir para a caverna) ou 2 (seguir o rio): ")

        # Verifica se o jogador escolheu a opção 1 (caverna)
        if escolha == "1":
            print("Você entrou na caverna e encontrou um urso!")
            # Pergunta se o jogador quer lutar com o urso
            lutar = input("Lutar (s/n)? ").lower()

            # Se o jogador escolher lutar E o número aleatório for maior que 0.5, ele vence
            if lutar == "s" and random.random() > 0.5:
                print("Você derrotou o urso e venceu!")
                break  # Termina o jogo com vitória
            else:
                # Caso contrário, o urso ataca e o jogador perde uma vida
                print("O urso te atacou!")
                vida -= 1

        # Verifica se o jogador escolheu a opção 2 (rio)
        elif escolha == "2":
            # Caminho seguro - jogador vence imediatamente
            print("Você seguiu o rio e encontrou uma vila segura!")
            print("Você venceu!")
            break  # Termina o jogo com vitória

        # Caso o jogador digite qualquer outra coisa que não 1 ou 2
        else:
            print("Escolha inválida!")

    # Se o loop terminar porque as vidas chegaram a 0 ou menos
    if vida <= 0:
        print("Fim de jogo! Você perdeu.")


# Chama a função para iniciar o jogo
jogo_aventura()