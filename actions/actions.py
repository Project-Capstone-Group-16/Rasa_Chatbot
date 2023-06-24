from .usecase import Usecase
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetAllWarehouseInfo(Action):

    def name(self) -> Text:
        return "ActionGetAllWarehouse"

    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        result = Usecase.GetAllWarehouse()
        
        dispatcher.utter_message(result) 

class ActionGetWarehouseByCity(Action):

    def name(self) -> Text:
        return "ActionGetWarehouseByCity"

    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        trackers  = tracker.get_latest_entity_values("city_name") 
        
        result = Usecase.GetWarehouseByCity(trackers)
        
        dispatcher.utter_message(result) 
