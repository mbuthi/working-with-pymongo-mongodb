from main import MongoConnection
import json
from datetime import datetime
connection = MongoConnection()

def find_station(my_station_id, my_num_hours):
    my_dict : dict = {}
    my_dict_2 : dict = {}
    pipeline : list = [
        {
            "$match" : {
                "station_status" : "In Service",
                "station_id" : my_station_id,                
            }            
        },
        {
            "$project" : {"station_name" : 1, "available_bikes" : 1, "time" : 1}            
        }        
    ]

    res : list = list(connection.retrieve_connection().aggregate(pipeline=pipeline))
    for station in res:        
        time = datetime.strptime(station.get("time"), "%Y/%m/%d %H:%M:%S").strftime("%H")        
        if time not in my_dict:
            my_dict[time]  = 1
        else: 
            my_dict[time]  += 1
        if station.get("available_bikes") == 0:
            if time not in my_dict_2:
                my_dict_2[time]  = 1
            else: 
                my_dict_2[time]  += 1
    sorted_dict : dict = sorted(my_dict_2.items(), key=lambda value : value[1], reverse=True)
    my_list = []
    for i in range(0, my_num_hours):
        my_list.append(sorted_dict[i])
    
    with open("./stations_dataset.json", "w") as file:
        for item in my_list:
            
            json_data = json.dumps(
                {
                    "hour" : item[0],
                    "percentage" : round(item[1] / my_dict[item[0]] * 100, 2),
                    "total_measurements" : my_dict[item[0]],
                    "zero_bikes_measurements" : item[1]
                }
            )
            file.write(json_data)
def main():
    find_station(my_station_id=522, my_num_hours=3)

if __name__ == "__main__":
    main()