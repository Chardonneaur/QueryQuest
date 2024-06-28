import json

# Open the file
with open('datafeed.json', 'r') as file:
    data = json.load(file)

    # Print the date and idvisit for each object
    for obj in data:
        date = obj['serverDatePretty']
        idvisit = obj['idVisit']
        print(f'Date: {date}, ID Visit: {idvisit}')
