import os, uuid
from turtle import bye
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from util import readAppSetting

blob_service_client = BlobServiceClient.from_connection_string(readAppSetting("storageConnectionString"))
blob_client = blob_service_client.get_blob_client(container="home-security-status", blob="status.json")

bytes = blob_client.download_blob().readall()
jsonObject = json.loads(bytes)
print (jsonObject["status"])
