import json

# Load the data from the JSON file
with open('1000.json') as f:
    data = json.load(f)

# Open a file for writing
with open('output.txt', 'w') as f:
    # Iterate over the data and print the date and browser
    for item in data:
        date = item['serverDatePretty']
        browser = item['browser']
        f.write(f"{date}\t{browser}\n")
