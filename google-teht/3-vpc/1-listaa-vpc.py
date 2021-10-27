from googleapiclient import discovery

def listaa_vpct(project_name):
  service = discovery.build('compute', 'v1')

  response = service.networks().list(project=project_name).execute()

  print(f"VPC:t projektissa {project_name}:")

  #jos vastauksessa on mitään
  if (response.get("items")):
    for network in response["items"]:
      print(f"Verkon nimi:   {network['name']}")
  else:
    print("Ei verkkoja")

#projekit voidaan määrittää käyttöliittymässä tai esim komentoriviltä parseargsilla
listaa_vpct("projektinnimi")