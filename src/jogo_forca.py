import random

def jogo_forca():
    palavras = ["python", "jogo", "programacao"]
    palavra = random.choice(palavras)
    letras_certas = ["_"] * len(palavra)
    erros = 0
    print("Bem-vindo ao Jogo da Forca!")
    while erros < 6 and "_" in letras_certas:
        print("Palavra:", " ".join(letras_certas))
        print(f"Erros: {erros}/6")
        letra = input("Digite uma letra: ").lower()
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_certas[i] = letra
        else:
            erros += 1
            print("Letra errada!")
    if "_" not in letras_certas:
        print(f"Parabéns! A palavra era {palavra}.")
    else:
        print(f"Perdeu! A palavra era {palavra}.")
jogo_forca()