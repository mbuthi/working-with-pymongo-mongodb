from main import MongoConnection
import json
connection = MongoConnection()

def find_station(my_time, my_station_id):
    my_query = {"station_id" : my_station_id, "time" : my_time}
    projection = {"station_name" : 1, "available_bikes" : 1}
    result = connection.retrieve_connection().find_one(my_query, projection)

    with open("./stations_dataset.json", mode="w") as file:
        file.write(
        json.dumps(
            {
                "station_name" : result.get("station_name"),
                "available_bikes" : result.get("available_bikes")
            }
        )
        
        )

def main():
    find_station(my_time="2019/06/09 12:30:00",my_station_id=2003)


if __name__ == "__main__":
    main()
    
    