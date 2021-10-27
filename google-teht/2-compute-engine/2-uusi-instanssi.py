import googleapiclient.discovery

#sisältää paljon huonoa placeholder-kommentointia
def create_instance(project_name, zone_name, instance_name):

    #käyttöönotetaan API
    compute = googleapiclient.discovery.build('compute', 'v1')

    print("Luodaan VM instanssi!")

    # Ubuntu Image
    image_response = compute.images().getFromFamily(
        project='ubuntu-os-cloud', family='ubuntu-1604-lts').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    # machinetype on f1-micro tässä tapauksessa
    machine_type = f'zones/{zone_name}/machineTypes/f1-micro'
    #ei määritellä startup scriptiä, mutta sen voisi määritellä tässä
    #startup_script = open(
        #os.path.join(
        #    os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    #image_url = "JOKU_URL"
    #image_caption = "KUVAUS"

    config = {
        'name': instance_name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }]#,

        # Jos metadata olisi määritelty ennen configia
        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        #'metadata': {
        #    'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                #'key': 'startup-script',
                #'value': startup_script
            #}, {
                #'key': 'url',
                #'value': image_url
            #}, {
                #'key': 'text',
                #'value': image_caption
            #}, {
                #'key': 'bucket', #tän voisi määritellä esim luontiskriptissä
                #'value': bucket
            #}]
        #}
    }

    return compute.instances().insert(
        project=project_name,
        zone=zone_name,
        body=config).execute()

#voidaan määritellä joko parseargsin avulla komentorivillä tai käyttöliittymässä
create_instance("projektinimi","zonenimi","instanssinimi")
