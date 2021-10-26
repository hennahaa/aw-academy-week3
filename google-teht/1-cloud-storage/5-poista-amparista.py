from google.cloud import storage

#https://cloud.google.com/storage/docs/deleting-objects#code-samples
def poista_amparista(amparinimi:str, tiedostonimi:str):

    storage_client = storage.Client()

    bucket = storage_client.bucket(amparinimi)
    blob = bucket.blob(tiedostonimi)
    blob.delete()

    print(f"Filu/blob {tiedostonimi} poistettu bucketista.")