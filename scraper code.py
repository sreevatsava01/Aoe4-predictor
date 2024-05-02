import requests
import json
import time
import datetime
import random
import os

page = 20

# URL of the API
url = "https://aoe4world.com/api/v0/games?updatedsince=2024-01-05T00:00:00.000Z&order=updated_at&leaderboard=rm_4v4&page="

directory = "data"

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' was created successfully.")

x = datetime.datetime.now()
timeName = x.strftime("%Y") + "-"+ x.strftime("%d") + "-"+ x.strftime("%b")

for p in range(page):
    sleepTime = 20 + random.random() * 10
    print(sleepTime)
    time.sleep(sleepTime)
    reqUrl = url + str(p + 1)    
# Send a GET request to the API
    response = requests.get(reqUrl)


    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data returned
        data = response.json()
        

        fileName = timeName + " page-" + str(p + 1) + ".json"
        
        file_path = os.path.join(directory, fileName)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))
        print("Data saved successfully.")
        # Optionally, you can process the data here or just print it out
        print(json.dumps(data, indent=4))
    else:
        print("Failed to retrieve data. Status code:", response.status_code)