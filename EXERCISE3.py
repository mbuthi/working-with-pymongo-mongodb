from main import MongoConnection
import pymongo
import json
connection = MongoConnection()


def find_station(my_time, my_zipcode):
    my_query = {"time" : my_time, "zipcode" : my_zipcode}
    projection = {"station_name" : 1, "available_bikes" : 1}

    res = connection.retrieve_connection().find(my_query, projection).sort("available_bikes", pymongo.DESCENDING)

    with open("./stations_dataset.json", mode="w") as file:
        for station in res:

            file.write(
                json.dumps(
                    {
                            "station_name" : station.get("station_name"),
                        "bikes" : station.get("available_bikes")            
                    }
                )
            
            )

def main():
    find_station(my_time="2019/06/10 12:45:00", my_zipcode=10022)

if __name__ == "__main__"    :
    main()