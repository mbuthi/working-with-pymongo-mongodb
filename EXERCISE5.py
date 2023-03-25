from main import MongoConnection
import json
import pymongo
connection = MongoConnection()

def find_station() -> None:
    pipeline = [
        
        {
            "$group" : {
                "_id" : "$borough" ,
                
                "num_stations" : {"$sum" : 1}

            }
        },
        {
            "$sort" : {
                "num_stations": pymongo.DESCENDING,
                "_id" : 1
            }
        }
    ]
    
    
    res = list(connection.retrieve_connection().aggregate(pipeline=pipeline))
    with open("./stations_dataset.json", "w") as file:
        for item in res:
            json_data = json.dumps({
                "borough" : item.get("_id"),
                "num_stations" : item.get("num_stations")
            })
            file.write(json_data)


def main() -> None:
    find_station()


if __name__ == "__main__":
    main()