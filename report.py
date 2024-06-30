
import pandas as pd

# Load the data from the JSON file
df = pd.read_json('data_source.json')

# Group by 'country' and count the occurrences
grouped = df.groupby('country').size().reset_index(name='count')

# Sort by 'count' in descending order and get the top 5
top_5 = grouped.sort_values('count', ascending=False).head(5)

# Export the top 5 to a CSV file
top_5.to_csv('output.csv', index=False)
