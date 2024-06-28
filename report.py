
import json
import matplotlib.pyplot as plt

# Load the data from the JSON file
with open('1000.json', 'r') as f:
    data = json.load(f)

# Extract the browserName dimension and count the occurrences
browser_names = [d['browserName'] for d in data]
browser_counts = {name: browser_names.count(name) for name in set(browser_names)}

# Create the pie chart
labels = browser_counts.keys()
sizes = browser_counts.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()
