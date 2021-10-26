from google.cloud import storage

#https://cloud.google.com/storage/docs/downloading-objects#storage-download-object-python
def lataa_amparista(amparinimi: str, tiedostonimi:str, latauskohde:str):
    # The path to which the file should be downloaded
    # latauskohde = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(amparinimi)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(tiedostonimi)
    blob.download_to_filename(latauskohde)

    print(f"Ladattiin filu {tiedostonimi} ämpäristä {amparinimi} nimellä {latauskohde}.")

print("Haetaan juttuja bucketista!")
amparinimi = input("Mikä bucket ID: ")
tiedostoid = input("Haettavan jutun ID: ")
tiedostonimi = input("Millä nimellä ladataan: ")

lataa_amparista(amparinimi,tiedostoid,tiedostonimi)