import requests
import json 
city = "kandedes"
endpoint = f"http://143.198.92.250:8080/warehouse?city={city}"

req = requests.get(url=endpoint, json="json")

response = json.loads(req.content)

lens = len(response["data"]) 
count_looping = 0
while count_looping < lens:
    print( f"{response[count_looping][]}") 
    count_looping += 1
