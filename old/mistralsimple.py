import os
from mistralai.client import MistralClient

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# Set the prompt
prompt = "Create a Python script where the source of the data is a file named 1000.json by using those dimensions: idVisit and make a simple report."

# Use the Mistral AI chat method to generate the API request URL
chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who writes python code and understands the content of a json file."},
        {"role": "user", "content": prompt}
    ]
)

# Print the response from Mistral AI
print(chat_response.choices[0].message.content)
