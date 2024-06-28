
import json

# Load data from the JSON file
with open('1000.json', 'r') as f:
    data = json.load(f)

# Initialize an empty dictionary to hold our report
report = {}

# Iterate over the data
for item in data:
    # Extract idSite and idVisit
    idSite = item.get('idSite')
    idVisit = item.get('idVisit')

    # If idSite is not in the report, add it
    if idSite not in report:
        report[idSite] = {}

    # If idVisit is not in the report for this idSite, add it
    if idVisit not in report[idSite]:
        report[idSite][idVisit] = 0

    # Increment the count for this idSite and idVisit
    report[idSite][idVisit] += 1

# Print the report
for idSite, visits in report.items():
    print(f'Site ID: {idSite}')
    for idVisit, count in visits.items():
        print(f'  Visit ID: {idVisit}, Count: {count}')
