
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the data from the JSON file
with open('data_source.json') as f:
    data = json.load(f)

# Convert the JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Count the frequency of each country
country_counts = df['country'].value_counts()

# Create a pie chart
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%')
plt.title('Most Popular Countries')
plt.show()

# Analysis
print("Analysis:")
print("The most popular countries on your website are:")
print(country_counts.head())
print("\nTo improve your website, you might want to consider adding more content or features that cater to these countries.")

# Export the data to a CSV file
df.to_csv('output.csv', index=False)
