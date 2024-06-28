import os
import re
import time
import subprocess
from mistralai.client import MistralClient

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# List of available dimensions
dimensions = ["idSite", "idVisit", "visitIp", "visitorId", "fingerprint", "type (actionDetails 0)", "url (actionDetails 0)", "pageTitle (actionDetails 0)", "pageIdAction (actionDetails 0)", "idpageview (actionDetails 0)", "serverTimePretty (actionDetails 0)", "pageId (actionDetails 0)", "timeSpent (actionDetails 0)", "timeSpentPretty (actionDetails 0)", "pageviewPosition (actionDetails 0)", "title (actionDetails 0)", "subtitle (actionDetails 0)", "icon (actionDetails 0)", "iconSVG (actionDetails 0)", "timestamp (actionDetails 0)", "dimension2 (actionDetails 0)", "dimension4 (actionDetails 0)", "dimension5 (actionDetails 0)", "goalConversions", "siteCurrency", "siteCurrencySymbol", "serverDate", "visitServerHour", "lastActionTimestamp", "lastActionDateTime", "siteName", "serverTimestamp", "firstActionTimestamp", "serverTimePretty", "serverDatePretty", "serverDatePrettyFirstAction", "serverTimePrettyFirstAction", "userId", "visitorType", "visitorTypeIcon", "visitConverted", "visitConvertedIcon", "visitCount", "visitEcommerceStatus", "visitEcommerceStatusIcon", "daysSinceFirstVisit", "secondsSinceFirstVisit", "daysSinceLastEcommerceOrder", "secondsSinceLastEcommerceOrder", "visitDuration", "visitDurationPretty", "searches", "actions", "interactions", "referrerType", "referrerTypeName", "referrerName", "referrerKeyword", "referrerKeywordPosition", "referrerUrl", "referrerSearchEngineUrl", "referrerSearchEngineIcon", "referrerSocialNetworkUrl", "referrerSocialNetworkIcon", "languageCode", "language", "deviceType", "deviceTypeIcon", "deviceBrand", "deviceModel", "operatingSystem", "operatingSystemName", "operatingSystemIcon", "operatingSystemCode", "operatingSystemVersion", "browserFamily", "browserFamilyDescription", "browser", "browserName", "browserIcon", "browserCode", "browserVersion", "totalEcommerceRevenue", "totalEcommerceConversions", "totalEcommerceItems", "totalAbandonedCartsRevenue", "totalAbandonedCarts", "totalAbandonedCartsItems", "events", "continent", "continentCode", "country", "countryCode", "countryFlag", "region", "regionCode", "city", "location", "latitude", "longitude", "visitLocalTime", "visitLocalHour", "daysSinceLastVisit", "secondsSinceLastVisit", "resolution", "plugins", "pluginIcon (pluginsIcons 0)", "pluginName (pluginsIcons 0)", "dimension1", "adClickId", "adProviderId", "adProviderName", "crashes", "customVariableName1 (customVariables 1)", "customVariableValue1 (customVariables 1)", "customVariableName2 (customVariables 2)", "customVariableValue2 (customVariables 2)", "customVariableName5 (customVariables 5)", "customVariableValue5 (customVariables 5)", "formConversions", "sessionReplayUrl", "campaignId", "campaignContent", "campaignKeyword", "campaignMedium", "campaignName", "campaignSource", "campaignGroup", "campaignPlacement"]

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
description = f"Create a Python script where the source of the data is a file named {filename} by using those dimensions: {', '.join(selected_dimensions)}. {report_type}."

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

# Execute the generated Python script
print("Executing report.py...")
result = subprocess.run(["python", "report.py"], capture_output=True, text=True)

# Print the output of the executed Python script
print("Output of report.py:")
print(result.stdout)
