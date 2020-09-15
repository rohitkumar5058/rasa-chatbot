# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:18:10 2020

@author: ashish_kumar2
"""

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import numpy as np
from word2number import w2n
import pathlib
import logging
logger = logging.getLogger(__name__)

        

class ActionTopWorld(Action):
    """Action for listing entities.
    The entities might be filtered by specific attributes."""

    def name(self):
        return "action_top_world"

    def run(self, dispatcher, tracker, domain):
        
        # first need to know the entity type we are looking for
        case_type = str.lower(tracker.get_slot("case_type"))
        cardinal = int(w2n.word_to_num(tracker.get_slot("CARDINAL")))
        
        # Read Data from csv
        logger.debug("Below is the Required Path")
        logger.debug(pathlib.Path().parent.absolute())
        logger.debug("Above was the Required Path")
        #print("Below is the Required Path")
        #print(pathlib.Path().parent.absolute())
        data_folder = pathlib.Path("/app/")
        file_to_open = data_folder / "covid_data_sample.csv"
        world_data= pd.read_csv(file_to_open,encoding = "ISO-8859-1")
        #world_data= pd.read_csv("/home/persistent.co.in/rohit_kumar1/compose/covid_data_sample.csv",encoding = "ISO-8859-1")
        
        # Sort data as per passed column and get the top results
        if (case_type=="confirmed"):
            world_data=world_data.sort_values(["total_cases"], ascending=False)
            dispatcher.utter_message(text="Showing results for top {0} countries as per {1} cases".format(cardinal,case_type))
            dispatcher.utter_message(text=str([str(x) for x in world_data.head(cardinal)['country']]))
        elif (case_type=="recovered" or case_type=="recovery"):
            world_data=world_data.sort_values(["total_recovered"], ascending=False)
            case_type = "recovered"
            dispatcher.utter_message(text="Showing results for top {0} countries as per {1} cases.".format(cardinal,case_type))
            dispatcher.utter_message(text=str([str(x) for x in world_data.head(cardinal)['country']]))
        elif (case_type=="death" or case_type=="deaths" or case_type=="deceased"):
            world_data=world_data.sort_values(["total_deaths"], ascending=False)
            case_type = "deaths"
            dispatcher.utter_message(text="Showing results for top {0} countries as per {1}.".format(cardinal,case_type))
            dispatcher.utter_message(text=str([str(x) for x in world_data.head(cardinal)['country']]))
        else:
            dispatcher.utter_message("Please specify if you are asking about Confirmed, Recovered ot Death Cases..!!")
        return []
        
