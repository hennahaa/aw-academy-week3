from google.cloud import storage

#https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-code_samples
def luo_ampari(ampari_nimi:str):
    #luo bucketin COLDLINE storage-classiin
    storage_client = storage.Client()

    bucket = storage_client.bucket(ampari_nimi)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(f"Luotiin bucket {new_bucket.name} sijaintiin {new_bucket.location} ja sillä on storage class: {new_bucket.storage_class}")

    return new_bucket

