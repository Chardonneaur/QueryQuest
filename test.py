import json
from collections import Counter

# Load data from the JSON file
with open('1000.json', 'r') as f:
    data = json.load(f)

# Extract URLs from actionDetails
urls = []
for item in data:
    if 'actionDetails' in item:
        for action in item['actionDetails']:
            if 'url' in action:
                urls.append(action['url'])

# Count occurrences of each URL
url_counts = Counter(urls)

# Print report
print("URL Report:")
for url, count in url_counts.items():
    print(f"{url}: {count}")
