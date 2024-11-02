import requests
from datetime import datetime as dt
USERNAME = "jashananeja"
TOKEN = "sahdadafjfj123djaisja"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


user_params ={
    "token" : TOKEN ,
    "username" : USERNAME ,
    "agreeTermsofService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url =pixela_endpoint ,json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID ,
    "name" : "Reading Graph" ,
    "unit" : "Pages",
    "type" : "int",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response =requests.post(url = graph_endpoint ,json = graph_config , headers = headers)
# print(response.text)
# https://pixe.la/v1/users/jashananeja/graphs/graph1.html


# posting value to graph
today_date = dt.now().strftime("%Y%m%d")

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date" : today_date,
    "quantity" : input("How many pages did you read today?") ,
    "optionalData" : "{\"note\": \"A night at Call-Center.\"}"
    
}
response = requests.post(url = pixel_creation_endpoint ,json= pixel_data ,headers= headers)
print(response.text)


# update the pixel

# update_endpoint = f"{pixel_creation_endpoint}/{dt.now().strftime("%Y%m%d")}"
# new_pixel_data = {
#     "quantity" : "5"
# }

# response = requests.put(url = update_endpoint , json =new_pixel_data , headers = headers)
# print(response.text)

#  Delete a pixel 

# update_endpoint = f"{pixel_creation_endpoint}/{dt.now().strftime("%Y%m%d")}"
# response = requests.delete(url = update_endpoint , headers= headers)
# print(response.text)



