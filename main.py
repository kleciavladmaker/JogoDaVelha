import random

tabuleiro = [0, 1, 2, 
       3, 4, 5,
       6, 7, 8]

def desenhar():
  print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
  print("-" * 9)
  print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
  print("-" * 9)
  print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

def jogadaHumano():
  while True:
    posicao = input("Escolha a posição: ")
    n = int(posicao)
  
    if(tabuleiro[n] == "X" or tabuleiro[n] == "O"):
      continue
    else:
      break
  tabuleiro[n] = "O"


def jogadaAI():
  print("Jogada da AI")
  opcoesValidas = []

  for i in range(0,9):
    if(tabuleiro[i] != "X" and tabuleiro[i] != "O"):
      opcoesValidas.append(i)

  opcao = random.choice(opcoesValidas)
  tabuleiro[opcao] = "X"

def ganhou(turno):
  if(
    # Avaliando as linhas
    (tabuleiro[0] == turno and tabuleiro[1] == turno and tabuleiro[2] == turno) or
    (tabuleiro[3] == turno and tabuleiro[4] == turno and tabuleiro[5] == turno) or
    (tabuleiro[6] == turno and tabuleiro[7] == turno and tabuleiro[8] == turno) or

# Avaliando as colunas
    (tabuleiro[0] == turno and tabuleiro[3] == turno and tab[6] == turno) or
    (tabuleiro[1] == turno and tabuleiro[4] == turno and tab[7] == turno) or
    (tabuleiro[2] == turno and tabuleiro[5] == turno and tab[8] == turno) or

#Avaliando as diagonais
    (tabuleiro[0] == turno and tabuleiro[4] == turno and tabuleiro[8] == turno) or(tabuleiro[2] == turno and tabuleiro[4] == turno and tabuleiro[6] == turno)

  ):
     return True
  else:
    return False


desenhar()

turnoHumano = True

for i in range(0, 9):
  if turnoHumano:
    jogadaHumano()
  
    if(ganhou("O")):
      desenhar()
      print("Jogador Humano ganhou")
      break
  else:
    jogadaAI()

    if(ganhou("X")):
      desenhar()
      print("AI Ganhou")
      break

  desenhar()
  turnoHumano = not turnoHumano

  if(i == 8):
    print("Deu Velha")



print("Fim do jogo.")