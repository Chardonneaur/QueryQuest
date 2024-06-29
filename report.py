
import json
from tabulate import tabulate

# Load the data from the JSON file
with open('1000.json') as f:
    data = json.load(f)

# Extract the required dimensions
table_data = [(item['serverDatePretty'], item['referrerType'], item['visitIp'], item['browser']) for item in data]

# Define the headers for the table
headers = ["Server Date", "Referrer Type", "Visit IP", "Browser"]

# Print the table
print(tabulate(table_data, headers=headers, tablefmt="grid"))
