import re
import requests

def get_matomo_url(instance_url, idSite, period, date, filter_limit, token_auth):
    base_url = f"{instance_url}/index.php?module=API&format=JSON"
    url = (f"{base_url}&idSite={idSite}&period={period}&date={date}&method=Live.getLastVisitsDetails"
           f"&filter_limit={filter_limit}&expanded=1&token_auth={token_auth}")
    return url

def parse_user_input(user_input):
    period = "range"
    date = user_input.strip()
    return period, date

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('datafeed.json', 'wb') as file:
            file.write(response.content)
        print("Data feed downloaded successfully as 'datafeed.json'.")
    else:
        print(f"Failed to download data feed. Status code: {response.status_code}")

def main():
    print("Welcome to the Matomo API URL generator!")

    instance_url = input("Please enter the instance URL (default: http://demo.matomo.cloud): ").strip()
    if not instance_url:
        instance_url = "http://demo.matomo.cloud"
    
    idSite = input("Please enter the site ID (default: 1): ").strip()
    if not idSite:
        idSite = "1"
    
    user_input = input("Please specify the date range (e.g., '2023-05-01,2023-05-31'): ").strip()
    
    filter_limit = input("Please enter the filter limit (e.g., 10): ").strip()
    token_auth = input("Please enter the token auth (default: anonymous): ").strip()
    if not token_auth:
        token_auth = "anonymous"

    period, date = parse_user_input(user_input)
    
    url = get_matomo_url(instance_url, idSite, period, date, filter_limit, token_auth)
    
    print("\nHere is your customized Matomo API URL:")
    print(url)
    
    execute = input("Do you want to execute this request and download the data feed? (yes/no): ").strip().lower()
    if execute == 'yes':
        download_data(url)
    else:
        print("Request not executed.")

if __name__ == "__main__":
    main()
