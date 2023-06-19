import requests
import json
import os
import random

url = "http://143.198.92.250:8080"
endpoint = f"{url}/bot"

class Database():
      def __init__(self):
            pass
      
      def GetAllWarehouseCityEP():
            endpoint = f"{endpoint}/warehouse"

            req = requests.get(url=endpoint, json="json")

            response = json.loads(req.content)

            return response
      
      def GetAllWarehousebyCityEP(city):
            endpoint = f"{endpoint}/warehouse"

            req = requests.get(url=endpoint, json="json")
      
            response = json.loads(req.content)
            
            return response
