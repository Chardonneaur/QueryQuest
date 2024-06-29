
import json

# Load data from the JSON file
with open('1000.json', 'r') as f:
    data = json.load(f)

# Assuming that 'data' is a list of dictionaries, we iterate over it
titles = []
for item in data:
    # Check if 'actionDetails' and 'title' keys exist in the dictionary
    if 'actionDetails' in item and 'title' in item['actionDetails']:
        titles.append(item['actionDetails']['title'])

# Generate a simple report
print("Report on actionDetails.title:")
for title in titles:
    print(f"- {title}")
