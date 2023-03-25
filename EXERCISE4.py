from main import MongoConnection
import json
import pymongo
connection = MongoConnection()

def find_station():
    

    pipeline = [

        {
            "$match" : {
                "station_status" : "In Service", 
                "available_bikes" : 0
            }
        },
        {
            "$group" : {
                "num_measurements": {"$sum": 1},
                "_id" : "$station_id"
                
            }
        }, 

        {
            "$sort" : {
                "num_measurements" : pymongo.DESCENDING
            }
        }
    ]
    
    response = connection.retrieve_connection().aggregate(pipeline=pipeline)
    
    response = next(response)

    with open("./stations_dataset.json", mode="w") as file:
        file.write(
            json.dumps(
                {
                    "num_measurements" : response.get("num_measurements"),
                    "station_id" : response.get("_id")        
                }
            )                        
        )

def main():
    find_station()

if __name__ == "__main__":
    main()