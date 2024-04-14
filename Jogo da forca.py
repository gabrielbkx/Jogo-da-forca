import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
palavras = ["abóbora", "girassol","piano",]

palavra_aleatoria = random.choice(palavras)
print(palavra_aleatoria)

display = []

vidas = 6

for letras in palavra_aleatoria:
    display += "_"

fim_de_jogo = False

while not fim_de_jogo:

    letra = input("Adivinhe uma letra\n").lower()

    for posicao in range (len(palavra_aleatoria)):
       letras = palavra_aleatoria[posicao]

       if letras == letra:
            display[posicao] = letras

    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_de_jogo = True
        print("Você Ganhou.")

    if letra not in palavra_aleatoria:
        vidas -= 1
        if vidas == 0:
            fim_de_jogo = True
            print("Você Perdeu.")

    print(stages[vidas])
  
teste replit app