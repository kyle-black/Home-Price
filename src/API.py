import requests
import keys

url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

querystring = {"city": "Austin", "state": "TX"}

headers = {
    "X-RapidAPI-Host": keys.rapid_api_host,
    "X-RapidAPI-Key": keys.rapid_api_key
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
