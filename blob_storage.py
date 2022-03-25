import json
from azure.storage.blob import BlobServiceClient, __version__
from util import readAppSetting

class BlobStorage:
    def __init__(self):
        connection_string = readAppSetting("storageConnectionString")
        containerName = "home-security-status"
        blobName = "status.json"
        blob_service_client = BlobServiceClient.from_connection_string(readAppSetting("storageConnectionString"))
        self.blob_client = blob_service_client.get_blob_client(container=containerName, blob=blobName)
    
    def GetStatus(self):
        bytes = self.blob_client.download_blob().readall()
        jsonObject = json.loads(bytes)
        return jsonObject["status"]



