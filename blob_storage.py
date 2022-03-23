import os, uuid
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from util import readAppSetting

blob_service_client = BlobServiceClient.from_connection_string(readAppSetting("storageConnectionString"))
blob_client = blob_service_client.get_blob_client(container="home-security-status", blob="status.json")
print("\nUploading to Azure Storage as blob")
data = {}
data['status'] = 'on'
json_data = json.dumps(data)
blob_client.upload_blob(json_data)