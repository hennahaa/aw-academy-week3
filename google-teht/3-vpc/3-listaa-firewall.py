from googleapiclient import discovery

def listaa_firewallit(project_name):
  service = discovery.build('compute', 'v1')

  response = service.firewalls().list(project=project_name).execute()

  print(f"Firewallit projektista {project_name}:")

  #jos vastauksessa on mitään
  if (response.get("items")):
    for firewall in response["items"]:
      print(f"Firewall nimi:   {firewall['name']}")
  else:
    print("Ei löytynyt mitään!")

#projektinimi voidaan määrittää käyttöliittymässä tai esim komentoriviltä parseargislla
listaa_firewallit("projektinnimi")