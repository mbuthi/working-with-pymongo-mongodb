from main import MongoConnection
import json
connection = MongoConnection()



def find_station():
    #find station data with station number 327
    my_query = {"station_id" : 327, "time" : "2019/06/09 12:15:00"}

    projection = {"station_name" : 1, "available_bikes" : 1}
    result = connection.retrieve_connection().find_one(my_query, projection)
        
        
    
    
    with open("stations_dataset.json", mode="w")    as file:

        file.write(
            json.dumps({
                "station_name" : result.get("station_name"),
                "bikes" : result.get("available_bikes")   
            })                        
        )

def main ():
    
    find_station()

if __name__ == "__main__":
    main()


    






