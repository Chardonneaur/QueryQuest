import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Set your Mistral AI API token
api_key = os.environ["MISTRAL_API_KEY"]

# Initialize the Mistral AI client with the API token
client = MistralClient(api_key=api_key)

# Prompt the user for the API request description
description = input("Explain the type of Python script that you would like to get:")

# Use the Mistral AI chat method to generate the API request URL
chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant who writes python code and understands the content of a json file composed like this: idSite,idVisit,visitIp,visitorId,fingerprint,type (actionDetails 0),url (actionDetails 0),pageTitle (actionDetails 0),pageIdAction (actionDetails 0),idpageview (actionDetails 0),serverTimePretty (actionDetails 0),pageId (actionDetails 0),timeSpent (actionDetails 0),timeSpentPretty (actionDetails 0),pageviewPosition (actionDetails 0),title (actionDetails 0),subtitle (actionDetails 0),icon (actionDetails 0),iconSVG (actionDetails 0),timestamp (actionDetails 0),dimension2 (actionDetails 0),dimension4 (actionDetails 0),dimension5 (actionDetails 0),goalConversions,siteCurrency,siteCurrencySymbol,serverDate,visitServerHour,lastActionTimestamp,lastActionDateTime,siteName,serverTimestamp,firstActionTimestamp,serverTimePretty,serverDatePretty,serverDatePrettyFirstAction,serverTimePrettyFirstAction,userId,visitorType,visitorTypeIcon,visitConverted,visitConvertedIcon,visitCount,visitEcommerceStatus,visitEcommerceStatusIcon,daysSinceFirstVisit,secondsSinceFirstVisit,daysSinceLastEcommerceOrder,secondsSinceLastEcommerceOrder,visitDuration,visitDurationPretty,searches,actions,interactions,referrerType,referrerTypeName,referrerName,referrerKeyword,referrerKeywordPosition,referrerUrl,referrerSearchEngineUrl,referrerSearchEngineIcon,referrerSocialNetworkUrl,referrerSocialNetworkIcon,languageCode,language,deviceType,deviceTypeIcon,deviceBrand,deviceModel,operatingSystem,operatingSystemName,operatingSystemIcon,operatingSystemCode,operatingSystemVersion,browserFamily,browserFamilyDescription,browser,browserName,browserIcon,browserCode,browserVersion,totalEcommerceRevenue,totalEcommerceConversions,totalEcommerceItems,totalAbandonedCartsRevenue,totalAbandonedCarts,totalAbandonedCartsItems,events,continent,continentCode,country,countryCode,countryFlag,region,regionCode,city,location,latitude,longitude,visitLocalTime,visitLocalHour,daysSinceLastVisit,secondsSinceLastVisit,resolution,plugins,pluginIcon (pluginsIcons 0),pluginName (pluginsIcons 0),dimension1,adClickId,adProviderId,adProviderName,crashes,customVariableName1 (customVariables 1),customVariableValue1 (customVariables 1),customVariableName2 (customVariables 2),customVariableValue2 (customVariables 2),customVariableName5 (customVariables 5),customVariableValue5 (customVariables 5),formConversions,sessionReplayUrl,campaignId,campaignContent,campaignKeyword,campaignMedium,campaignName,campaignSource,campaignGroup,campaignPlacement."),
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
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
data = response.json()
print(f"API response: {data}")
