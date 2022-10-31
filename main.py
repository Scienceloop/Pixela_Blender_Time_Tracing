import requests
from datetime import datetime

USERNAME= "user"
TOKEN= "token"
GRAPHID = "graph1"

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_congig = {
    "id": GRAPHID,
    "name": "Blender",
    "unit": "Minutes",
    "type": "float",
    "color": "shibafu"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response1 = requests.post(url=graph_endpoint, json=graph_congig, headers=headers)

today = datetime.now()

pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Hours did you spent on Blender today? ")
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

response = requests.post(url=pixel_endpoint, json=pixel, headers=headers)

print(response.text)