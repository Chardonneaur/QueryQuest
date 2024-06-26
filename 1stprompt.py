import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# Prompt the user for the API request description
description = input("Enter a description of the API request you want to make (e.g. 'Get the number of visits for the last 30 days using the Live.getLastVisitsDetails method for site ID 1 and token anonymous'): ")

# Use the Mistral AI chat method to generate the API request URL
chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant that generates Matomo API request URLs for the Live.getLastVisitsDetails method based on user-provided descriptions. The Live.getLastVisitsDetails method allows you to retrieve detailed information about the last visits to a website, including the number of visits, the visit duration, and the actions performed during the visit. To use this method, you need to specify the website ID and authentication token in the API request. You can also specify the date range for which you want to retrieve the visit data."),
        ChatMessage(role="user", content="Here's an example of how to use the Live.getLastVisitsDetails method to get the number of visits for the last 30 days:"),
        ChatMessage(role="assistant", content="To get the number of visits for the last 30 days using the Live.getLastVisitsDetails method, you can use the following API request URL: `https://demo.matomo.cloud/index.php?module=API&method=Live.getLastVisitsDetails&idSite=1&period=day&date=last30&format=JSON&token_auth=anonymous`"),
        ChatMessage(role="user", content=description)
    ]
)

# Extract the generated API request URL from the chat response
url = chat_response.choices[0].message.content.strip()

# Print the API request URL
print(f"API request URL: {url}")

# Send the API request and print the response
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
data = response.json()
print(f"API response: {data}")
