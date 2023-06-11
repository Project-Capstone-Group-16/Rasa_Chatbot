from .DatabaseEndpointConfig import Database 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class Repository:
    def GetAllWarehouseByCity():
        response = Database.GetAllWarehouse()
        json = len(response["inventron"])        
        tampung = []

        count = 0

        while c < json:

            tampung.append(json["inventron"][count]['warehouses']['city']) 
            c += 1

        return tampung