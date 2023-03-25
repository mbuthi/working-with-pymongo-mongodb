# working-with-pymongo-mongodb
This repository contains code snippets showcasing the working of Mongo DB with python


#### EXERCISE1

Compute the station_name of the station_id 327 as well as its number of available_bikes at time
"2019/06/09 12:15:00".


#### EXERCISE2

Given a concrete time and station_id passed as parameters (variables my_time and my_station_id,
respectively), compute the station_name with such id as well as its number of available_bikes at that
given time.


#### EXERCISE3

Given a concrete time and zipcode passed as parameters (variables my_time and my_zipcode,
respectively), compute the station_name of all stations having such zipcode, including the number of
available_bikes of each of them at that given time. Order the results by decreasing order in the number
of available_bikes.


#### EXERCISE4

Considering only the subset of documents of the dataset where station_status = "In Service" and
available_bikes = 0, compute the amount of documents (num_measurements) per station_id. Present the
results including only the station_id with highest number of documents (highest num_measurements).


#### EXERCISE5

Each station_id belongs to a single borough. Compute the number of different station_id per borough.
Order the results by decreasing amount of stations and, in case of tie, by lexicographic order in the
borough name.


#### EXERCISE6

Given a concrete station_id and num_hours passed as parameters (variables my_station_id and
my_num_hours, respectively), and considering only the subset of documents of the dataset where
station_status = "In Service" and station_id = my_station_id:
- Compute the percentage of documents with available_bikes = 0 for each hour of the day (e.g.,
for the period [8am, 9am) the percentage is 15.06% and for the period [9am, 10am) the
percentage is 27.32%).
- Sort the percentage results in decreasing order.
- Present the results only with the top num_hours documents.

