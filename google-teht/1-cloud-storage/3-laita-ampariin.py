from google.cloud import storage

#https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample
def laita_ampariin(amparinimi:str, tiedostonimi:str, uusi_nimi:str):

    # The path to your file to upload
    # source_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(amparinimi)
    blob = bucket.blob(uusi_nimi)

    blob.upload_from_filename(tiedostonimi)

    print(f"Tiedosto {tiedostonimi} ladattu bucketiin {amparinimi} nimellä {uusi_nimi}.")
