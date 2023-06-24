from .repository import Repository 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class Usecase:
    def __init__(self):
        pass

    def GetAllWarehouse():
        response = Repository.GetAllWarehouse()
        json = len(response["data"])        
        result = []

        count = 0

        while count < json:

            result.append(response["data"][count]["city"]) 
            count += 1
        
        a = (', '.join(result))

        return f"Berikut adalah daftar Kota yang memiliki outlet Inventron {a}"
    
    def GetWarehouseByCity(city):
        response = Repository.GetWarehousebyCity(city)
        json = len(response["data"])

        result = (f"Ya, outlet Inventron tersedia di kota {city}")

        if json > 0 :
            result

        else :
            result = (f"Mohon maaf untuk sementara inventron tidak tersedia di kota {city}")
        
        return result 
    

