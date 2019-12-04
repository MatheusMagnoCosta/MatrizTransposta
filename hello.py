import os

def gerarMatriz():
  matriz = [[],[],[],[]]
  matrizT = [[],[],[],[]]
  m = matriz
  for l in range(4):
    for c in range(4):
      numero = int(input("Valor: "))
      matriz[l].append(numero)
      matrizT[l].append(numero)
      os.system('cls' if os.name == 'nt' else 'clear')
      print("linha: ",l+1," ",matriz[l])
  transposta(matriz,matrizT)
  
def transposta(m,mt): 
  os.system('cls' if os.name == 'nt' else 'clear')
  for l in range(len(m)):
    for c in range(len(m[l])):
      mt[l][c] = m[c][l]
  print(mt[0])
  print(mt[1])
  print(mt[2])
  print(mt[3])
gerarMatriz()