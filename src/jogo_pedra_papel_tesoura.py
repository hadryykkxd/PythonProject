import random

def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    print("Bem-vindo ao Pedra, Papel, Tesoura!")
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para parar): ").lower()
        if jogador == "sair":
            break
        if jogador not in opcoes:
            print("Escolha inválida!")
            continue
        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")
        else:
            print("Computador venceu!")
jogo_pedra_papel_tesoura()