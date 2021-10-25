import requests

response = requests.get("https://api.github.com/search/repositories?q=language:python")

data = response.json()
#pyöritetään vain itemsin alla olevaa dataa
item_data = data["items"]

lista = []
#kaivetaan dictistä tiedot listaan
for i in range(len(item_data)):
  forkit = item_data[i]["forks"]
  nimi = item_data[i]["name"]
  kuvaus = item_data[i]["description"]
  lista.append((forkit,nimi,kuvaus))

#järjestetään listan tuplen ekan arvon eli forkin mukaan
lista.sort(key = lambda x:x[0], reverse=True)

for projekti in lista:
  print(f"{projekti[0]}.{projekti[1]}:{projekti[2]}")