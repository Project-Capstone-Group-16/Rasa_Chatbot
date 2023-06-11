import requests
import json
import os
import random

url = "http://143.198.92.250:8080"
endpoint = f"{url}/get/warehouse/"

class Database():
      def __init__(self):
            pass

      def GetAllWarehousebyCity(city):
            endpoint = f"{endpoint}{city}"

            requests = requests.get(url=endpoint, json="json")
            
            response = json.loads(requests.content)
            
            return response

      def GetAllWarehousebyFavorite():
            endpoint = f"{endpoint}/favorite"