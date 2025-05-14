# Define a função principal do jogo de perguntas
def jogo_perguntas():
    # Dicionário contendo as perguntas (chaves) e respostas (valores)
    perguntas = {
        "Qual é a capital de Portugal?": "lisboa",
        "Em que ano Python foi criado?": "1991",
        "Qual é minha fav linguagem": "python"
    }

    # Mensagem de boas-vindas ao jogo
    print("Bem-vindo ao Jogo de Perguntas!")

    # Inicializa a pontuação do jogador em zero
    pontuacao = 0

    # Loop que percorre cada pergunta e resposta no dicionário
    for pergunta, resposta in perguntas.items():
        # Exibe a pergunta atual
        print(pergunta)

        # Obtém a resposta do jogador e converte para minúsculas
        palpite = input("Sua resposta: ").lower()

        # Verifica se a resposta do jogador está correta
        if palpite == resposta:
            print("Correto!")  # Mensagem de acerto
            pontuacao += 1  # Incrementa a pontuação
        else:
            # Mensagem de erro mostrando a resposta correta
            print(f"Errado! A resposta era {resposta}.")

    # Exibe a pontuação final do jogador (acertos/total de perguntas)
    print(f"Sua pontuação: {pontuacao}/{len(perguntas)}")


# Chama a função para iniciar o jogo
jogo_perguntas()