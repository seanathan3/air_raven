import http.client

conn = http.client.HTTPSConnection("travel-advisor.p.rapidapi.com")

payload = "{\"contentType\":\"hotel\",\"contentId\":\"4172546\",\"questionId\":\"8393250\",\"pagee\":0,\"updateToken\":\"\"}"

headers = {
    'x-rapidapi-key': "838acae028msh99bfae513199ebbp1415a4jsn4ae8b5fc2bb8",
    'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/answers/v2/list?currency=USD&units=km&lang=en_US", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))