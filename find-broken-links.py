import json
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#ChromeDriver 111.0.5563.64
chromedriver_path = "./chromedriver.exe"

# List of URLs to check
urls = ["https://www.google.com/", 
        "https://www.facebook.com/", 
        "https://www.amazon.com/", 
        "https://melanienavarro.com/"]

# Set up desired capabilities for Chrome WebDriver
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

# Create a new Chrome WebDriver instance with the desired capabilities
browser = WebDriver(chromedriver_path, desired_capabilities=capabilities)


# Function to extract the HTTP status code from network logs
def get_status(logs, url):
    for log in logs:
        if log['message']:
            log_message = json.loads(log['message'])
            try:
                # Check if the content type is HTML and if a response was received
                content_type = 'text/html' in log_message['message']['params']['response']['headers']['content-type']
                response_received = log_message['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    # Extract and print the HTTP status code
                    status = log_message['message']['params']['response']['status']
                    print(status)
                    print(f"Status code for {url} is {status}")
                    return status
            except:
                pass

# Loop through each URL and check its status code
for url in urls:
    try:
        browser.get(url)
        logs = browser.get_log('performance')
        status_code = get_status(logs, url)
    except:
        # If an exception occurred, print an error message
        print(f"{url} is a broken link")

# Quit the Chrome WebDriver instance
browser.quit()