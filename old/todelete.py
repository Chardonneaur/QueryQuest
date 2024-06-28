import json

with open("1000.json", "r") as f:
    data = json.load(f)

visitor_ids = set(item["visitorId"] for item in data)

print("Visitor ID Report:")
for visitor_id in visitor_ids:
    print(visitor_id)
