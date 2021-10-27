import googleapiclient.discovery

def list_instances(project_name, zone_name):
    
    #Käyttöönotetaan API
    compute = googleapiclient.discovery.build('compute', 'v1')

    print("VM instanssit määritetyllä alueella:")

    #Tulostetaan instanssit, response on json, jossa name ja status ovat itemsin sisässä
    response = compute.instances().list(project=project_name, zone=zone_name).execute()

    print(f"Instanssit projektissa {project_name}, jotka ovat zonella {zone_name}:")
    #jos responsessa on jotain sisässä
    if (response.get('items')):
        for instance in response['items']:
            print(f"Nimi:         {instance['name']}")
            print(f"Status:       {instance['status']}")
            print()
    else:
        print('Ei instansseja')


#projektin nimen tai instanssin zonen voi pyytää käyttöliittymässä
#tai komentorivillä käyttäen argparsea
list_instances("projektinimi","instanssizone")