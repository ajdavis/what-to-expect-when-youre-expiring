def fn():
    client = pymongo.MongoClient()
    1 / 0  # Oops.
    print(client.server_info())
