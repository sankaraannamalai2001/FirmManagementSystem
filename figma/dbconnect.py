from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    client = MongoClient(CONNECTION_STRING)
    return client['Firm']
db=get_database()
col = db["login"]