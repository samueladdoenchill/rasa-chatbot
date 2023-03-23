from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


ALLOWED_SIZES = [
    "small",
    "medium",
    "large",
    "extra-large",
]
ALLOWED_TYPES = ["mozzarella", "fungi", "veggie", "pepperoni", "hawaii"]
ALLOWED_BRANDS = ["Levi's","Tommy Hilfiger","Polo","Calvin Klein"]
ALLOWED_SEX = ["male","female"]
ALLOWED_OCCASSIONS = ["formal","casual","work","sports","special","do not specify"]
ALLOWED_PRODUCTS = ["shirt","trouser","jeans","skirt"," do not specify"]




ALLOWED_CONFIRMATIONS = ["yes","no"]

class AskForPizzaTypeAction(Action):
    def name(self) -> Text:
        return "action_ask_type"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"What kind of pizza do you want?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_TYPES],
        )
        return []
    
class AskForPizzaSizeAction(Action):
    def name(self) -> Text:
        return "action_ask_size"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"May I know the preferred size of your pizza?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_SIZES],
        )
        return []
    
class AskForProductAction(Action):
    def name(self) -> Text:
        return "action_ask_product"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"Can you please tell me the product you would prefer?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_PRODUCTS],
        )
        return []

class AskForBrandAction(Action):
    def name(self) -> Text:
        return "action_ask_brand"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"Please, do you have a specific brand in mind?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_BRANDS],
        )
        return []

class AskForOccasionAction(Action):
    def name(self) -> Text:
        return "action_ask_occasion"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"Do you have an occasion in mind?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_OCCASSIONS],
        )
        return []
    
class AskForSexAction(Action):
    def name(self) -> Text:
        return "action_ask_sex"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text=f"Who is wearing the shirt?",
            buttons=[{"title": p, "payload": p} for p in ALLOWED_SEX],
        )
        return []


class ValidateSImplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"
    
    def validate_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `size` value."""

        if slot_value not in ALLOWED_SIZES:
            dispatcher.utter_message(text=f"We only accept pizza sizes: {'/'.join(ALLOWED_SIZES)}.")
            return {"size": None}
        return {"size": slot_value}

    def validate_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `type` value."""

        if slot_value not in ALLOWED_TYPES:
            dispatcher.utter_message(
                text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_TYPES)}."
            )
            return {"type": None}
        # if not slot_value:
        #     dispatcher.utter_message(
        #         text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
        #     )
        #     return {"pizza_type": None}
        # dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"type": slot_value}
    
class ValidateProductForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_product_form"
    
    def validate_product(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product` value."""

        if slot_value not in ALLOWED_PRODUCTS:
            dispatcher.utter_message(text=f"Sorry, We only have these products: {'/'.join(ALLOWED_PRODUCTS)}.")
            return {"product": None}
        return {"product": slot_value}
    
    def validate_brand(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `brand` value."""

        if slot_value not in ALLOWED_BRANDS:
            dispatcher.utter_message(text=f"Sorry, We only have these brands: {'/'.join(ALLOWED_BRANDS)}.")
            return {"brand": None}
        return {"brand": slot_value}
    
    def validate_occasion(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `occasion` value."""

        if slot_value not in ALLOWED_OCCASSIONS:
            dispatcher.utter_message(text=f"Sorry, We only have products for these occasion: {'/'.join(ALLOWED_OCCASSIONS)}.")
            return {"occasion": None}
        return {"occasion": slot_value}

    def validate_sex(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `sex` value."""

        if slot_value not in ALLOWED_SEX:
            dispatcher.utter_message(text=f"Sorry, I don't recgonize that gender: {'/'.join(ALLOWED_SEX)}.")
            return {"sex": None}
        return {"sex": slot_value}
    
    def validate_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `size` value."""

        if slot_value not in ALLOWED_SIZES:
            dispatcher.utter_message(text=f"We only accept pizza sizes: {'/'.join(ALLOWED_SIZES)}.")
            return {"size": None}
        return {"size": slot_value}