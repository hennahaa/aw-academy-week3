from pprint import pprint
from googleapiclient import discovery

def luo_vpc(project_name):
  service = discovery.build('compute', 'v1')

  network_body = {
    "name": "testi-verkko",
    "autoCreateSubnetworks": False,
    "routingConfig": {
      "routingMode": "REGIONAL"
    }
  }

  request = service.networks().insert(project=project_name, body=network_body)
  response = request.execute()

  pprint(response)

#projektinimi voidaan määrittää käyttöliittymässä tai esim parseargsilla komentorivillä
luo_vpc("projektinnimi")