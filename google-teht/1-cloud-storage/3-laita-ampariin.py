from google.cloud import storage

#https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample
def laita_ampariin(amparinimi:str, tiedostonimi:str, uusinimi:str):

    # The path to your file to upload
    # source_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(amparinimi)
    blob = bucket.blob(uusinimi)

    blob.upload_from_filename(tiedostonimi)

    print(f"Tiedosto {tiedostonimi} ladattu bucketiin {amparinimi} nimellä {uusinimi}.")

print("Laitetaan tiedosto bucketiin!")
amparinimi = input("Bucketin nimi: ")
tiedostonimi = input("Tiedoston polku: ")
uusinimi = input("Millä nimellä tallennetaan: ")

laita_ampariin(amparinimi, tiedostonimi, uusinimi)