
import json
from collections import defaultdict
from datetime import datetime

# Load data from JSON file
with open('1000.json', 'r') as f:
    data = json.load(f)

# Initialize containers for our report
country_count = defaultdict(int)
referrer_count = defaultdict(int)
date_count = defaultdict(int)

# Process data
for item in data:
    country_count[item['country']] += 1
    referrer_count[item['referrerType']] += 1
    date_count[datetime.strptime(item['serverDate'], '%Y-%m-%d').date()] += 1

# Print report
print("Country report:")
for country, count in country_count.items():
    print(f"{country}: {count}")

print("\nReferrer type report:")
for referrer, count in referrer_count.items():
    print(f"{referrer}: {count}")

print("\nServer date report:")
for date, count in date_count.items():
    print(f"{date}: {count}")
