import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"

querystring = {"query":"new"}

headers = {
	"x-rapidapi-key": "838acae028msh99bfae513199ebbp1415a4jsn4ae8b5fc2bb8",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())