import os
import re
import time
from mistralai.client import MistralClient

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

# Set the filename of the JSON data source
filename = "1000.json"

# Format the selected dimensions, report type, and filename into a string
description = f"Create a Python script where the source of the data is a file named {filename} by using those dimensions: {', '.join(selected_dimensions)} and {report_type}."

# Print the prompt that will be sent to Mistral AI
print("Prompt:", description)

# Use the Mistral AI chat method to generate the API request URL
chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who writes python code and understands the content of a json file."},
        {"role": "user", "content": description}
    ]
)

# Wait for 2 seconds before continuing with the script
time.sleep(2)

# Print the response from Mistral AI
print("Response:", chat_response.choices[0].message.content)

# Extract the Python script from the Mistral AI response
python_script = chat_response.choices[0].message.content
match = re.search("`python(.*?)```", python_script, re.DOTALL)
if match is None:
    print("Error: Mistral AI did not generate a Python script in its response.")
    exit()
else:
    python_script = match.group(1)

# Modify the generated Python script to load the data from the specified file
python_script = python_script.replace("data.json", filename)

# Save the generated Python script to a file
with open('report.py', 'w') as f:
    f.write(python_script)

# Print the location of the saved Python script
print(f"Python script saved to report.py")

# Print the contents of report.py to the console
with open('report.py', 'r') as f:
    print(f.read())
