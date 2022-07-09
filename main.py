import requests
from datetime import datetime

pixela_api = "https://pixe.la/v1/users"
api_key = "hlhlhlhlhlhlhlhlhlhlhlh"

#creating an account
parameters = {
    "token": api_key,
    "username": "sahilraj",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_api, json=parameters)
# print(response.text)

#creating a graph
graph_api = "https://pixe.la/v1/users/sahilraj/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "coding status",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

header = {
    "X-USER-TOKEN": api_key
}

# response = requests.post(url=graph_api, json=graph_parameters, headers=header)

#updating the graph:
print("hi! Whats your status")
user = input("post/change/delete: ")
today = datetime.now()
date = today.strftime("%Y%m%d")

if user == "post":
    update_api = f"{pixela_api}/sahilraj/graphs/graph1"
    update_parameters = {
        "date": date,
        "quantity": input("how many hours did you code today?: ")
    }

    response = requests.post(url=update_api, json=update_parameters, headers=header)
    print(response.text)

elif user == "change":
    change_api = f"{pixela_api}/sahilraj/graphs/graph1/{date}"
    change_parameters = {
        "quantity": input("Quantity u wanna change: ")
    }

    response = requests.put(url=change_api, json=change_parameters, headers=header)
    print(response.text)

elif user == "delete":
    delete_api = f"{pixela_api}/sahilraj/graphs/graph1/{date}"
    response = requests.delete(url=delete_api, headers=header)
    print(response.text)