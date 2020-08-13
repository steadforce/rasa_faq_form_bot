from typing import List, Text, Any, Dict, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class HotelForm(FormAction):

    def name(self) -> Text:
        return "hotel_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "number_of_persons",
             "date",
             "nights",
            "room_type"
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "number_of_persons": [self.from_entity(entity="number", intent=["inform"])],
            "date": [self.from_entity(entity="date", intent=["inform", "request_room"])],
            "nights": [self.from_entity(entity="days", intent=["inform"])],
        }
