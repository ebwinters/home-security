from azure.data.tables import TableClient, UpdateMode

class TableStorage:
    def __init__(self, tableName):
        connection_string = ""
        self.tableClient = TableClient.from_connection_string(conn_str=connection_string, table_name=tableName)

    def SetShouldMonitorFlag(self, shouldMonitor):
        entity = {
            u'PartitionKey': u'flags',
            u'RowKey': u'ShouldMonitor',
            u'ShouldMonitor': shouldMonitor
        }
        self.tableClient.update_entity(mode=UpdateMode.REPLACE, entity=entity)

    def GetShouldMonitorFlag(self):
        my_filter = "PartitionKey eq 'flags'"
        shouldMonitor = False
        entities = self.tableClient.query_entities(my_filter)
        for entity in entities:
            for key in entity.keys():
                if (key == "ShouldMonitor"):
                    shouldMonitor = entity["ShouldMonitor"]
        return shouldMonitor

tableStorage = TableStorage("homesecflags")
x = tableStorage.GetShouldMonitorFlag()
print(x)