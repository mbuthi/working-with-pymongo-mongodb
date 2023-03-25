import pymongo
import json
from dotenv import load_dotenv
import os
load_dotenv()

USERNAME = os.getenv("MY_USERNAME")
PASSWORD = os.getenv("MY_PASSWORD")
CLUSTER = os.getenv("MY_CLUSTER")
SERVER_DOMAIN = os.getenv("SERVER_DOMAIN")
class MongoConnection:
    def __init__(self) -> None:
        self.db = None

    def connect(self):
        client = pymongo.MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER}.{SERVER_DOMAIN}/?retryWrites=true&w=majority",  connectTimeoutMS=60000)
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
        




