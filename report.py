
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load data from JSON file
with open('1000.json', 'r') as file:
    data = json.load(file)

# Extract the 'country' values and count the occurrences
countries = [d['country'] for d in data]
country_counts = pd.value_counts(countries)

# Plot a pie chart
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%')
plt.title('Country Distribution')
plt.axis('equal')
plt.show()

# Save the data to a CSV file
country_counts.to_csv('country_counts.csv', header=['Count'])
