import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# List of available dimensions
dimensions = ["idSite", "idVisit", "visitIp", "visitorId", "fingerprint"]

# Prompt the user for the dimensions
selected_dimensions = []
while True:
    dimension = input(f"Choose a dimension from this list: {', '.join(dimensions)} or type 'no' to proceed: ")
    if dimension.lower() == "no":
        break
    elif dimension in dimensions:
        selected_dimensions.append(dimension)
    else:
        print("Invalid input. Please try again.")

# Prompt the user for the type of report they want
report_type = input("What would you like to do with the selected dimensions? (e.g., group them, make a pie chart, etc.): ")

# Format the selected dimensions and report type into a string
description = f"Create a Python script for a report with these dimensions: {', '.join(selected_dimensions)} and {report_type} them."

# Use the Mistral AI chat method to generate the API request URL
chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant who writes python code and understands the content of a json file."),
        ChatMessage(role="user", content="You can only write in Python, you never use the row number in the script, No text between or after. No ```python. The data source will be a json file"),
        ChatMessage(role="assistant", content="Explain how you would like the report to look like."),
        ChatMessage(role="user", content=description)
    ]
)

# Extract the generated API request URL from the chat response
url = chat_response.choices[0].message.content.strip()

# Print the API request URL
print(f"API request URL: {url}")

# Send the API request and print the response
import requests
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
data = response.json()
print(f"API response: {data}")
