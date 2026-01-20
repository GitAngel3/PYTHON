"""You are helping a travel blog store and manage recent trip details. Each trip includes a city name,
the date it was visited (in the format dd-mm-yyyy), and a short comment. Your task is to:
Create a Python module named tripdata.py with a function that returns trip details in dictionary format.
In your main file, import the function and use it to build a list of trip dictionaries.
For each trip:
  Convert the date string into a date object.
   Format the date to display as "Month Day, Year" (e.g., “May 15, 2023”).
Convert the list of trip dictionaries to a JSON string and print it."""

# main.py

from tripdata import get_trip
from datetime import datetime
import json

# Build list of trips
trips = [
    get_trip("Paris", "15-05-2023", "Amazing food and culture"),
    get_trip("Tokyo", "02-11-2024", "Loved the city lights"),
    get_trip("Rome", "10-03-2022", "History everywhere")
]

# Process each trip
for trip in trips:
    # Convert string to date object
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    # Format date as "Month Day, Year"
    trip["date"] = date_obj.strftime("%B %d, %Y")

# Convert list of dictionaries to JSON
json_output = json.dumps(trips, indent=4)

print(json_output)
