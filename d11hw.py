from datetime import datetime
import json
def get_record(city, comment, visit_date):
    return {
        "city": city,
        "comment": comment,
        "date": visit_date
    }
records = [
    get_record("Paris", "Beautiful city", "15-05-2023"),
    get_record("Tokyo", "Amazing food", "20-09-2024"),
    get_record("London", "Historic places", "10-01-2025")
]
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")
json_data = json.dumps(records, indent=4)
print(json_data)
parsed_records = json.loads(json_data)
for record in parsed_records:
    print(record)