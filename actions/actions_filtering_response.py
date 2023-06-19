from .actions_request_database import Database 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class Repository:
    def __init__(self):
        pass

    def GetAllWarehouseByCity(city):
        response = Database.GetAllWarehousebyCityEP(city)
        json = len(response["inventron"])        
        result = []

        count = 0

        while c < json:

            result.append(json["inventron"][count]['warehouses']['city']) 
            c += 1

        return result


    def GetWarehousebyCity(city):
        response = Database.GetAllWarehousebyCityEP(city)
        json = len(response["inventron"])        
        result = []

        count = 0
        
        while c < json:

            result.append(json["inventron"][count]['warehouses']['city']) 
            c += 1


        return result        
        

        