import requests
import json
import os
import random



class Repository():
      def __init__(self):
            pass
      
      def GetAllWarehouse():
            endpoint = "http://143.198.92.250:8080/warehouse"

            req = requests.get(url=endpoint, json="json")

            response = json.loads(req.content)

            return response
      
      def GetWarehousebyCity(city):
            endpoint = f"http://143.198.92.250:8080/warehouse?city={city}"

            req = requests.get(url=endpoint, json="json")
      
            response = json.loads(req.content)
            
            return response
