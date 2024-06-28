import json
import csv
from collections import defaultdict

# Open the JSON file
with open('1000.json') as f:
    data = json.load(f)

# Create a defaultdict to store the grouped data
grouped_data = defaultdict(list)

# Iterate over the data and group it by the date and browser
for item in data:
    date = item['serverDatePretty']
    browser = item['browser']
    grouped_data[(date, browser)].append(item)

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['Date', 'Browser'])

    # Iterate over the grouped data and write it to the CSV file
    for (date, browser), items in grouped_data.items():
        writer.writerow([date, browser])
