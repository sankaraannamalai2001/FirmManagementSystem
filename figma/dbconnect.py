from pymongo import MongoClient
def get_database():
    #CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    CONNECTION_STRING = "mongodb+srv://firm:firm@cluster0.sakjm.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(CONNECTION_STRING)
    return client['Firm']
db=get_database()
col = db["login"]