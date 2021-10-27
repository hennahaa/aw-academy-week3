from pprint import pprint
from googleapiclient import discovery

def luo_firewall(project_name):
  service = discovery.build('compute', 'v1')
  
  #päästää läpi TCP:22 portista tagilla testitag
  firewall_body = {
    "name": "testi-firewall",
    "targetTags": [
      "testitag"
    ],
    "allowed": [
      {
      "ports": [
        "22"
      ],
      "IPProtocol": "tcp"
      }
    ],
    "direction": "INGRESS"
  }

  request = service.firewalls().insert(project=project_name, body=firewall_body)
  response = request.execute()

  pprint(response)

#projekti voidaan määrittää käyttöliittymässä tai esim komentoriviltä parseargsilla
luo_firewall("projektinnimi")