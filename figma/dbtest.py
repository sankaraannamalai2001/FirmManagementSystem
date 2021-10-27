def get_database():
    from pymongo import MongoClient
    import pymongo


    #CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)


    return client['first']



if __name__ == "__main__":
    # Get the database
    dbname = get_database()
    collection_name = dbname["collection1"]
    item_1 = {
        "name": "Blender",
        "price": 340,
        "category": "kitchen appliance"
    }

    item_2 = {
        "name": "Egg",
        "category": "food",
        "price": 36,
    }
    collection_name.insert_many([item_1, item_2])