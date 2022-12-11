from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.events import FollowupAction, EventType, SlotSet, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionSlotReset(Action):
    def name(self) -> Text:
        return "action_slot_reset"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return[
            SlotSet("just_text", None),
            SlotSet("see", None),
            SlotSet("hear", None),
            SlotSet("touch", None),
            SlotSet("smell", None),
            SlotSet("emotion", None),
            SlotSet("feeling1", None),
            SlotSet("trigger1", None),
            SlotSet("trigger2", None),
            SlotSet("activity_question1", None),
            SlotSet("activity_question2", None),
            SlotSet("activity_question3", None),
            SlotSet("activity_question4", None),
            SlotSet("story", None),
            SlotSet("story1", None),
            SlotSet("story2", None),
            SlotSet("feel_more_control", None)
            ]

class TriggerWords(Action):
    
    def name(self) -> Text:
        return "action_trigger"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        trigger = tracker.get_slot('just_text')
        list = ['sucide', 'kill', 'die', 'sucidal', 'kill myself', 'end my life']
        t = trigger.split()
        for i in list:
            if i in t:
                buttons = []
                buttons.append({"title": 'HR' , "payload": 'hr'})
                buttons.append({"title": 'Professional' , "payload": 'professional'})
                dispatcher.utter_message(text = "Hey I sense a trigger word would you like to take this up with your HR or a professional?", buttons=buttons)
                return [FollowupAction('action_listen')]
        return []
                 

class ActionName(Action):
    
    def name(self) -> Text:
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        if name:
            return [FollowupAction('utter_greet_option')]
        return [FollowupAction('name_form')]


class ActionCapitalize(Action):
    
    def name(self) -> Text:
        return "action_capitalize"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        name = str.title(name)
        return [SlotSet("name", name)]


class ActionSelfCare(Action):
    
    def name(self) -> Text:
        return "action_self_care"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        selfcares = json.load(open('selfcare.json'))

        items = []

        for selfcare in selfcares.items():
            item = {
                "title": f"{selfcare[0]}",
                "subtitle": f"{selfcare[1][0]}",
                "image_url": f"{selfcare[1][1]}",
                "buttons": [
                    {
                    "title": "Start",
                    "type": "postback",
                    "payload": f"/{selfcare[1][2]}"
                    }
                ]
            }
            items.append(item)
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": items
            }}
        dispatcher.utter_message(text = "", attachment=message)

        return []


class ActionActivity(Action):
    
    def name(self) -> Text:
        return "action_activities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activities = json.load(open('activity.json'))
        items = []

        for activity in activities.items():
            item = {
                "title": f"{activity[0]}",
                "subtitle": f"{activity[1][0]}",
                "image_url": f"{activity[1][1]}",
                "buttons": [
                    {
                    "title": "Schedule",
                    "type": "postback",
                    "payload": "/schedule"
                    }
                ]
            }
            items.append(item)
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": items
            }}
        dispatcher.utter_message(text = "", attachment=message)
        return []


class ActionRelaxation(Action):
    
    def name(self) -> Text:
        return "action_relaxation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        relaxations = json.load(open('relaxation.json'))
        items = []

        for relaxation in relaxations.items():
            item = {
                "title": f"{relaxation[0]}",
                "subtitle": f"{relaxation[1][0]}",
                "image_url": f"{relaxation[1][1]}",
                "buttons": [
                    {
                    "title": "Start",
                    "type": "postback",
                    "payload": f"/{relaxation[1][2]}"
                    }
                ]
            }
            items.append(item)
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": items
            }}
        dispatcher.utter_message(text = "", attachment=message)
        return []
    

class ActionQuestion(Action):
    
    def name(self) -> Text:
        return "action_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('activity_question_form')]

class ActionFeelMoreControl(Action):
    
    def name(self) -> Text:
        return "action_feel_more_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('feel_more_control_form')]

class ActionStory2(Action):
    
    def name(self) -> Text:
        return "action_story2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('story2_form')]

class ActionStory(Action):
    
    def name(self) -> Text:
        return "action_story"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('story_form')]

class ActionStory1(Action):
    
    def name(self) -> Text:
        return "action_story1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('story1_form')]

class ActionTrigger1(Action):
    
    def name(self) -> Text:
        return "action_trigger1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('trigger1_form')]

class ActionTrigger_1(Action):
    
    def name(self) -> Text:
        return "action_trigger_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        trigger = tracker.get_slot('trigger1')

        dispatcher.utter_message(text = "Why do you think '" + trigger + "'' upsets you?")

        return [FollowupAction('trigger1_1_form')]

class ActionTrigger3(Action):
    
    def name(self) -> Text:
        return "action_trigger3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        trigger = tracker.get_slot('trigger2')

        dispatcher.utter_message(text = "Why do you think '" + trigger + "'' upsets you?")

        return [FollowupAction('trigger2_1_form')]

class ActionTrigger2(Action):
    
    def name(self) -> Text:
        return "action_trigger2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('trigger2_form')]

class ActionFeeling1(Action):
    
    def name(self) -> Text:
        return "action_feeling1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('feeling1_form')]

class ActionSee(Action):
    
    def name(self) -> Text:
        return "action_see"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('see_form')]

class ActionTouch(Action):
    
    def name(self) -> Text:
        return "action_touch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('touch_form')]

class ActionHear(Action):
    
    def name(self) -> Text:
        return "action_hear"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('hear_form')]

class ActionSmell(Action):
    
    def name(self) -> Text:
        return "action_smell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('smell_form')]

class ActionEmotion(Action):
    
    def name(self) -> Text:
        return "action_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('emotion_form')]

class ActionEmotion2(Action):
    
    def name(self) -> Text:
        return "action_emotion_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [FollowupAction('utter_done')]

class ActionFavoriteRelaxation(Action):
    
    def name(self) -> Text:
        return "action_favorite_relaxation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        favorite_relaxation = tracker.get_slot('favorite_relaxation')

        if favorite_relaxation:
            return [FollowupAction('utter_favorite_relaxation')]
        return [FollowupAction('utter_question')]

class ActionDia(Action):
    
    def name(self) -> Text:
        return "action_dia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        favorite_relaxation = tracker.get_slot('favorite_relaxation')
        if not favorite_relaxation == 'slow_diaphragmatic_breathing':
            return [FollowupAction("utter_slow_diaphragmatic_breathing_6")]
        return [FollowupAction('utter_do_next')]

class ActionMind(Action):
    
    def name(self) -> Text:
        return "action_mind"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        favorite_relaxation = tracker.get_slot('favorite_relaxation')
        if not favorite_relaxation == 'mindfulness_exercise':
            return [FollowupAction("utter_mindfulness_exercise_6")]
        return [FollowupAction('utter_do_next')]

class ActionPMR(Action):
    
    def name(self) -> Text:
        return "action_pmr"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        favorite_relaxation = tracker.get_slot('favorite_relaxation')
        if not favorite_relaxation == 'p_m_r':
            return [FollowupAction("utter_p_m_r_6")]
        return [FollowupAction('utter_do_next')]


class ActionFavoriteRelaxation(Action):
    
    def name(self) -> Text:
        return "action_favorite_relaxation_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        favorite_relaxation = tracker.get_slot('favorite_relaxation')

        if favorite_relaxation == 'slow_diaphragmatic_breathing':
            return [FollowupAction('utter_slow_diaphragmatic_breathing_1')]
        if favorite_relaxation == 'mindfulness_exercise':
            return [FollowupAction('utter_mindfulness_exercise_1')]
        if favorite_relaxation == 'p_m_r':
            return [FollowupAction('utter_p_m_r_1')]
        
class ActionActivity(Action):
    
    def name(self) -> Text:
        return "action_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        aq1 = tracker.get_slot('activity_question1')
        aq2 = tracker.get_slot('activity_question2')
        aq3 = tracker.get_slot('activity_question3')
        aq4 = tracker.get_slot('activity_question4')
        answer = [aq1, aq2, aq3, aq4]

        adic = json.load(open('answer.json'))
        activities = json.load(open('activity.json'))

        
        for alist in adic.items():
            if answer == alist[1]:
                result = alist[0]

        for activity in activities.items():
            if result == activity[0]:
                message = {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": f"{activity[0]}",
                                "subtitle": f"{activity[1][0]}",
                                "image_url": f"{activity[1][1]}",
                                "buttons": [
                                    {
                                    "title": "Start",
                                    "type": "postback",
                                    "payload": "/greet"
                                    }
                                ]
                            }
                        ]
                    }
                }
                dispatcher.utter_message(text = "We recommend you do this activity.", attachment=message)
        return []