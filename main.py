import random
from Jogo_da_forca_Arte import stages,logo
from Jogo_da_forca_palavras import palavras

palavra_aleatoria = random.choice(palavras)
print(logo)

display = []

vidas = 6

for letras in palavra_aleatoria:
    display += "_"

fim_de_jogo = False

print(palavra_aleatoria)

while not fim_de_jogo:

    letra = input("Adivinhe uma letra\n").lower()

    if letra in display:
        print(f"Você ja digitou a letra {letra}")

    for posicao in range (len(palavra_aleatoria)):
       letras = palavra_aleatoria[posicao]

       if letras == letra:
            display[posicao] = letras

    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_de_jogo = True
        print("Você Ganhou.")

    if letra not in palavra_aleatoria:
        print(f"A letra {letra} não esta na Palavra,Você Perdeu uma vida")
        vidas -= 1

        if vidas == 0:
            fim_de_jogo = True
            print("Você Perdeu.")
            print(f"A palavra era {palavra_aleatoria}")

    print(stages[vidas])
  
