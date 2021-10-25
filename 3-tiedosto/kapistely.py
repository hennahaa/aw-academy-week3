sanalista = []

#luetaan tiedosto
try:
  with open("sanat.txt") as tiedosto:
    for rivi in tiedosto:
      rivi = rivi.replace("\n", "")
      sanalista.append(rivi)
except IOError:
  print("Tiedoston avaamisessa kävi jotain hupsua!")

#järjestetään sisältö
def jarjestys(str):
  return len(str), str.lower()

jarjestetty_sanalista = sorted(sanalista, key=jarjestys)

try:
  with open("sorted_sanat.txt", "w") as jarjestetty_tiedosto:
    for sana in jarjestetty_sanalista:
      jarjestetty_tiedosto.write(sana+"\n")
except IOError:
  print("Tiedoston kirjoittamisessa kävi jotain hupsua!")