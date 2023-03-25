import pymongo
import json
class MongoConnection:
    def __init__(self) -> None:
        self.db = None

    def connect(self):
        client = pymongo.MongoClient("mongodb+srv://shareapp311:2XE6GdQH1pYpkx7i@cluster0.s6uofda.mongodb.net/?retryWrites=true&w=majority",  connectTimeoutMS=60000)
        return client
    
    def retrieve_database(self):
        db = self.connect().my_database
        return db

    def retrieve_connection(self):
        return self.retrieve_database().my_citibike_collection
        

class LoadData():
    def __init__(self) -> None:
        self.connection = MongoConnection()
        
    def load_working_data(self):
        data = []
        with open("./stations_dataset.json", mode="r") as file:
            data = file.readlines()
        new_data : list = [json.loads(item) for item in data]
        self.connection.retrieve_connection().insert_many(new_data)
        




