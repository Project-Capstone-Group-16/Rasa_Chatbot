
from .actions_filtering_response import Repository
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")


class ActionGetWarehouseByCity(Action):

    def name(self) -> Text:
        return "ActionGetWarehouseByCity"

    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker):
        
        trackers  = tracker.get_latest_entity_values("city_name") 
        
        result = Repository.GetAllWarehouseByCity(trackers)
        
        count_looping = 0
        
        dispatcher.utter_message(text = f"Berikut adalah daftar cabang Inventron yang sudah beroprasi") 

        while count_looping < 0:
                    dispatcher.utter_message(text = f"{result[count_looping]}") 
                    count_looping += 1


class ActionGetAllWarehouseInfo(Action):

    def name(self) -> Text:
        return "ActionGetWarehouseAvailibility"

    def run (self, dispatcher: CollectingDispatcher,
            tracker: Tracker):
        
        trackers  = tracker.get_latest_entity_values("city_name") 
        
        result = Repository.GetAllWarehouseByCity(trackers)
        
        list_count = len(result)
        
        if list_count < 1 :

            dispatcher.utter_message(f"Mohon maaf untuk sementara Inventron tidak tersedia di kota {trackers}")
        
        else :

            count_looping = 0
            
            while count_looping < list_count :
                    dispatcher.utter_message(text = f"ya inventron tersedia pada kota {result[count_looping]} berikut alamat Inventron cabang ") 
                    count_looping += 1


