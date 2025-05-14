import random

def jogo_aventura():
    print("Bem-vindo à Aventura na Floresta!")
    print("Você está numa floresta. Escolha seu caminho.")
    vida = 3
    while vida > 0:
        print(f"Vida: {vida}")
        escolha = input("Digite 1 (ir para a caverna) ou 2 (seguir o rio): ")
        if escolha == "1":
            print("Você entrou na caverna e encontrou um urso!")
            lutar = input("Lutar (s/n)? ").lower()
            if lutar == "s" and random.random() > 0.5:
                print("Você derrotou o urso e venceu!")
                break
            else:
                print("O urso te atacou!")
                vida -= 1
        elif escolha == "2":
            print("Você seguiu o rio e encontrou uma vila segura!")
            print("Você venceu!")
            break
        else:
            print("Escolha inválida!")
    if vida <= 0:
        print("Fim de jogo! Você perdeu.")
jogo_aventura()