
import json
from collections import defaultdict
from tabulate import tabulate

# Function to read data from the JSON file
def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Function to process the data and create a report
def create_report(data):
    report = defaultdict(list)

    for entry in data:
        country = entry.get('country')
        server_date = entry.get('serverDate')

        if country and server_date:
            report[country].append(server_date)

    return dict(sorted(report.items()))

# Function to print the report table
def print_report_table(report):
    headers = ['Country', 'Server Dates']
    rows = []

    for country, dates in report.items():
        rows.append([country, ', '.join(dates)])

    print(tabulate(rows, headers=headers, tablefmt='pipe'))

if __name__ == '__main__':
    json_file = '1000.json'
    data = read_json_file(json_file)
    report = create_report(data)
    print_report_table(report)
