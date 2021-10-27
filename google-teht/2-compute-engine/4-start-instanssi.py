import googleapiclient.discovery

#käynnistetään VM instanssi
def start_instance(instance_name, project_name, zone_name):

    # Käyttöönotetaan api
    compute = googleapiclient.discovery.build('compute', 'v1')

    #tämän voi toisaalta tehdä esim niin että pysäytetään instanssin nimellä
    print(f"Käynnistetään VM instanssi {instance_name}.")

    # Start VM instance
    compute.instances().start(
          project=project_name,
          zone=zone_name,
          instance=instance_name).execute()

    return
    
#nää voi pyytää käyttöliittymässä tai argparsella komentorivillä
start_instance("instanssinimi","projektinimi","zonenimi")