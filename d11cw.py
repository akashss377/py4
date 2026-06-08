from datetime import datetime
import json
def get_trip(city, visit_date):
    return {
        "city": city,
        "date": visit_date
    }
trips = [
    get_trip("Paris", "15-05-2023"),
    get_trip("Tokyo", "20-09-2024"),
    get_trip("London", "10-01-2025")
]
for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    trip["date"] = date_obj.strftime("%B %d, %Y")
json_data = json.dumps(trips, indent=4)
print(json_data)