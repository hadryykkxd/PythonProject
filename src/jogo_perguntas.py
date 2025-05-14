def jogo_perguntas():
    perguntas = {
        "Qual é a capital de Portugal?": "lisboa",
        "Em que ano Python foi criado?": "1991",
        "Qual é a linguagem do TGPSI?": "python"
    }
    print("Bem-vindo ao Jogo de Perguntas!")
    pontuacao = 0
    for pergunta, resposta in perguntas.items():
        print(pergunta)
        palpite = input("Sua resposta: ").lower()
        if palpite == resposta:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Errado! A resposta era {resposta}.")
    print(f"Sua pontuação: {pontuacao}/{len(perguntas)}")
jogo_perguntas()