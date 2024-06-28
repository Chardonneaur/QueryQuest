import os
import openai

# Set your OpenAI API key
api_key = os.environ["OPENAI_API_KEY"]

# Initialize the OpenAI client with the API token
openai.api_key = api_key

# List of available dimensions
dimensions = ["idSite", "idVisit", "visitIp", "visitorId", "fingerprint", "serverDate"]

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

# Format the selected dimensions into a string
description = "Create a Python script for a report with these dimensions: " + ", ".join(selected_dimensions)

# Use the OpenAI chat method to generate the API request URL
response = openai.ChatCompletion.create(
    model="gpt-3.5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who writes python code and understands the content of a json file."},
        {"role": "user", "content": "You can only write in Python, you never use the row number in the script, No text between or after. No ```python. The data source will be a json file."},
        {"role": "assistant", "content": "Explain how you would like the report to look like."},
        {"role": "user", "content": description}
    ]
)

# Extract the generated Python script from the chat response
generated_script = response.choices[0].message['content'].strip()

# Print the generated Python script
print(f"Generated Python script:\n{generated_script}")

# Optionally, save the generated script to a file
with open("generated_script.py", "w") as file:
    file.write(generated_script)

# The generated script can be further modified or executed as needed
