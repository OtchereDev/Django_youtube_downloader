import requests

url = "https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D"

headers = {
    'x-rapidapi-key': "7786dc6809msh413859170edd552p1229c0jsn280cc9d870bf",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)