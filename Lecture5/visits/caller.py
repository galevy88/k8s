import time
import requests

url = "http://3.234.215.104:4001/"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Response received:", response.text)
        else:
            print("Failed to retrieve data:", response.status_code)
    except requests.RequestException as e:
        print("Error:", str(e))
    
    # Pause for 2 seconds before the next request
    time.sleep(2)
