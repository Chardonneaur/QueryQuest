import os
import json
import re
import subprocess
import requests
from mistralai.client import MistralClient
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# Load the list of available dimensions from a JSON file
with open('dimension_list.json') as f:
    dimensions = json.load(f)

# Initialize the list of selected dimensions
selected_dimensions = []

# Create a WordCompleter for the dimensions
completer = WordCompleter(dimensions)

# Prompt the user to select dimensions with autocompletion
while True:
    dimension = prompt('Choose a dimension from this list: ' + ', '.join(dimensions) + ' or type \'no\' to proceed: ', completer=completer)
    if dimension == 'no':
        break
    elif dimension in dimensions:
        selected_dimensions.append(dimension)
    else:
        print("Invalid input. Please try again.")

# Format the selected dimensions, report type, and filename into a string
if any(dim.startswith('actionDetails.') for dim in selected_dimensions):
    action_details_handling = "If any dimension starts with 'actionDetails.', handle this dimension specifically by iterating through the 'actionDetails' array within each item."
else:
    action_details_handling = ""

# Prompt the user for the type of report they want
report_type = input("What would you like to do with the selected dimensions? (e.g., group them, make a pie chart, etc.): ")

# Define the base URL
base_url = "https://demo.matomo.cloud"

# Prompt the user for the date range
start_date = input("Enter the start date (format: YYYY-MM-DD): ") or "2024-01-01"
end_date = input("Enter the end date (format: YYYY-MM-DD): ") or "2024-01-01"

# Construct the URL path with the date range
url_path = f"/index.php?module=API&format=JSON&period=range&date={start_date},{end_date}&method=Live.getLastVisitsDetails&filter_limit=1000&expanded=1"

# Prompt the user for the idSite and token_auth
id_site = input("Enter the idSite (default is 1): ") or "1"
token_auth = input("Enter the token_auth: ")

# Construct the URL
url = f"{base_url}{url_path}&idSite={id_site}&token_auth={token_auth}"

# Download the data from the URL
response = requests.get(url)

# Save the data to a file named 'data_source.json'
with open('data_source.json', 'w') as f:
    f.write(response.text)

# Set the filename of the JSON data source
filename = "data_source.json"

description = f"Create a Python script where the source of the data is a file named {filename} by using those dimensions: {', '.join(selected_dimensions)}. {report_type}. {action_details_handling} From those data, give me your analysis in order to improve my website. At the end, export the data as a CSV file named 'output.csv'."

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

# Save the generated Python script to a file
with open('report.py', 'w') as f:
    f.write(python_script)

# Print the location of the saved Python script
print(f"Python script saved to report.py")

# Print the contents of report.py to the console
with open('report.py', 'r') as f:
    print(f.read())

# Execute the generated Python script
print("Executing report.py...")
result = subprocess.run(["python", "report.py"], capture_output=True, text=True)

# Print the output of the executed Python script
print("Output of report.py:")
print(result.stdout)
