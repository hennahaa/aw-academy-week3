import statistics

syote = input("Syötä rivi pilkulla eroteltuja lukuja: ")

#muodostetaan syötteestä lista
luvut = syote.split(",")
#pyöräytetään lista vielä int-muotoon
luvut = [int(luku) for luku in luvut]

print(f"Luvuista pienin on: {min(luvut)}")
print(f"Luvuista suurin on: {max(luvut)}")
print(f"Lukujen keskiarvo on: {sum(luvut)/len(luvut)}")
print(f"Lukujen moodi on: {statistics.mode(luvut)}")
print(f"Lukujen mediaani on: {statistics.median(luvut)}")

