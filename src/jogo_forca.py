# Importa o módulo random para seleção aleatória
import random


# Define a função principal do jogo da forca
def jogo_forca():
    # Lista de palavras possíveis para o jogo
    palavras = ["python", "jogo", "programacao"]

    # Seleciona aleatoriamente uma palavra da lista
    palavra = random.choice(palavras)

    # Cria lista de underscores representando letras não descobertas
    letras_certas = ["_"] * len(palavra)

    # Inicializa contador de erros
    erros = 0

    # Mensagem de boas-vindas
    print("Bem-vindo ao Jogo da Forca!")

    # Loop principal: continua enquanto houver tentativas restantes e letras por descobrir
    while erros < 6 and "_" in letras_certas:
        # Exibe o estado atual da palavra (com letras descobertas e underscores)
        print("Palavra:", " ".join(letras_certas))

        # Mostra quantos erros o jogador já cometeu (máximo 6)
        print(f"Erros: {erros}/6")

        # Solicita uma letra ao jogador e converte para minúscula
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra está na palavra secreta
        if letra in palavra:
            # Percorre a palavra para revelar todas as ocorrências da letra
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_certas[i] = letra  # Substitui o underscore pela letra correta
        else:
            # Incrementa o contador de erros se a letra não existir na palavra
            erros += 1
            print("Letra errada!")

    # Verifica condição de vitória (nenhum underscore restante)
    if "_" not in letras_certas:
        print(f"Parabéns! A palavra era {palavra}.")
    else:
        # Mensagem de derrota se o jogador esgotou as tentativas
        print(f"Perdeu! A palavra era {palavra}.")


# Inicia o jogo chamando a função principal
jogo_forca()