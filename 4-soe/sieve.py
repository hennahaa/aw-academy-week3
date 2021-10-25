#Sieve of Eratosthenes
def alkuluvut(raja):

  #alustetaan  bool-lista jossa kaikki on true kunnes toisin todistetaan
  alkuluku = [True] * (raja+1)
  luku = 2

  #kunhan käsiteltävän luvun tulo itsensä kanssa on pienempi kuin syötetty raja
  while (luku * luku <= raja):

    #jos käsiteltävä luku on alkuluku, täytyy sen kertoimet käsitellä
    if alkuluku[luku] == True:
    
      #kaikki luvun kertoimet ovat False
      #range(start, stop, step)
      for i in range(luku*luku, raja+1, luku):
        alkuluku[i] = False

    #käsitellään seuraava luku
    luku += 1

  for luku in range(2,raja+1):
    if alkuluku[luku] == True:
      print(luku, end=" ")

syote = int(input("Anna raja: "))

alkuluvut(syote)