import random
def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número (1 a 10): "))
        tentativas += 1
        if palpite == numero_secreto:
            print(f"Parabéns! Acertou em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior!")
        else:
            print("Tente um número menor!")
jogo_adivinhacao()