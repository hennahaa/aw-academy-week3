import googleapiclient.discovery

#pysäytetään VM instanssi
def stop_instance(instance_name, project_name, zone_name):

    # Käyttöönotetaan API
    compute = googleapiclient.discovery.build('compute', 'v1')

    #tämän voi toisaalta tehdä esim niin että pysäytetään instanssin nimellä
    print(f"Pysäytetään VM instanssi {instance_name}.")

    # Pysäytetään VM instanssi
    compute.instances().stop(
          project=project_name,
          zone=zone_name,
          instance=instance_name).execute()

    return

#nää voi pyytää käyttöliittymässä tai argparsella komentorivillä
stop_instance("instanssinimi","projektinimi","zonenimi")