"""You are building a simple activity tracker for a travel blog. Each time a traveler visits a place, the system stores the city name, a visit comment, and the visit date in the format "dd-mm-yyyy".
Your task is to:
Create a module called tracker.py that contains a function to return a travel record (as a dictionary).
In the main file, use the function to create a list of at least 3 travel records.
Convert the date string of each record into a readable format like "Month Day, Year" (e.g., "June 05, 2022").
Convert the list of records into a JSON string and print it.
Parse the JSON back to a Python object and display each record on a separate line.

"""


from tracker import create_record
from datetime import datetime
import json

records = [
    create_record("Paris", "Loved the Eiffel Tower", "05-06-2022"),
    create_record("Rome", " history place", "18-08-2023"),
    create_record("Tokyo", "Scenary was incredible", "10-04-2024")
]


for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON Output:")
print(json_data)


parsed_data = json.loads(json_data)

print("\nParsed Records:")
for rec in parsed_data:
    print(f'{rec["city"]} | {rec["comment"]} | {rec["date"]}')
