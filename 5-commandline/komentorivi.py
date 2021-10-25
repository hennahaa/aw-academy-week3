import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operaatio", help="määrittää laskutoimituksen! Joko summa, erotus, tulo tai jako")
parser.add_argument("ekaluku", help="ensimmäinen luku laskutoimituksessa", type=int)
parser.add_argument("tokaluku", help="toinen luku laskutoimituksessa", type=int)
args = parser.parse_args()

if args.operaatio == "summa":
  print("Kokonaislukujen summa on:", args.ekaluku+args.tokaluku)

if args.operaatio == "erotus":
  print("Kokonaislukujen erotuus on:", args.ekaluku-args.tokaluku)

if args.operaatio == "tulo":
  print("Kokonaislukujen tulo on:", args.ekaluku*args.tokaluku)

if args.operaatio == "jako":
  print("Kokonaislukujen karkea kokonaislukuun pyöristetty jakolasku on:", args.ekaluku//args.tokaluku)
