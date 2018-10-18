

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from IPython.core.display import Image, display

import requests

class ApiAction(Action):
    def name(self):
        return "action_paper_search"

    def run(self, dispatcher, tracker, domain):

        paper_type = tracker.get_slot('paper_type')
        
        response = requests.get('http://dblp.org/search/publ/api?q={}&format=json&h=1'.format(paper_type)).json()
        title = response['result']['hits']['hit'][0]['info']['title']
        authors = response['result']['hits']['hit'][0]['info']['authors']['author'][0]
        link = response['result']['hits']['hit'][0]['info']['url']

        dispatcher.utter_message("I found a paper called {}".format(title))
        return [SlotSet("link",link), SlotSet("authors",authors)]
        
