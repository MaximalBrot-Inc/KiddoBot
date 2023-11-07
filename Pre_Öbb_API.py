import requests

headers = {"Channel": "inet",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}
url = "https://shop.oebbtickets.at/api/domain/v4/init"
response = requests.get(url,headers=headers)
data = response.json()
Acces_Token = data["accessToken"]
print(Acces_Token)




url2 = "https://shop.oebbtickets.at/api/hafas/v1/stations"
payload2_ = {"longitude": "11777763","latitude": "47390175"}
payload2 = {"name": "Wien"}
headers2 = {
            "AccessToken": Acces_Token,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }
response2 = requests.get(url2, headers=headers2, params=payload2)
print(response2.url)
data2 = response2
print(data2.content)

