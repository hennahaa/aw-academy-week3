from google.cloud import storage

#https://cloud.google.com/storage/docs/listing-buckets#storage-list-buckets-python
def listaa_amparit():
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()
    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

listaa_amparit()