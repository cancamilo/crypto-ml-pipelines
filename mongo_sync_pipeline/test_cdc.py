from pymongo import MongoClient


def insert_data_to_mongodb(uri, database_name, collection_name, data):
    """
    Insert data into a MongoDB collection.

    :param uri: MongoDB URI
    :param database_name: Name of the database
    :param collection_name: Name of the collection
    :param data: Data to be inserted (dict)
    """
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]

    try:
        # result = collection.insert_one(data)
        result = collection.insert_many(data)
        print(f"Data inserted with _id: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    mongodb_uri = "mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set"
    database_name = "scrabble"
    collection_name = "test"
    test_data = [{"name": "local test 2"}, {"name": "local test 3"}]
    insert_data_to_mongodb(mongodb_uri, database_name, collection_name, test_data)
