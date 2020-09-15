## welcome message
* get_started
  - utter_get_started
  
## greet and exit
* greet
  - utter_greet
* goodbye
  - utter_goodbye


## top 10 confirmed cases
* greet
    - utter_greet
* top_world{"CARDINAL": "10", "case_type": "confirmed"}
    - slot{"CARDINAL": "10"}
    - slot{"case_type": "confirmed"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top ten confirmed cases (ten in words)
* greet
    - utter_greet 	
* top_world{"case_type": "confirmed", "CARDINAL": "ten"}
    - slot{"CARDINAL": "ten"}
    - slot{"case_type": "confirmed"}
    - action_top_world
* goodbye
	- utter_goodbye

## top 10 recovered cases
* greet
    - utter_greet
* top_world{"CARDINAL": "10", "case_type": "recovered"}
    - slot{"CARDINAL": "10"}
    - slot{"case_type": "recovered"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top ten confirmed cases (ten in words)
* greet
    - utter_greet 	
* top_world{"case_type": "recovered", "CARDINAL": "ten"}
    - slot{"CARDINAL": "ten"}
    - slot{"case_type": "recovered"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top 5 cases as per recovery
* greet
    - utter_greet 	
* top_world{"case_type": "recovery", "CARDINAL": "5"}
    - slot{"CARDINAL": "5"}
    - slot{"case_type": "recovery"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top 3 cases as per deaths
* greet
    - utter_greet 	
* top_world{"case_type": "deaths", "CARDINAL": "3"}
    - slot{"CARDINAL": "3"}
    - slot{"case_type": "deaths"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top 3 cases as per death
* greet
    - utter_greet 	
* top_world{"case_type": "death", "CARDINAL": "3"}
    - slot{"CARDINAL": "3"}
    - slot{"case_type": "death"}
    - action_top_world
* goodbye
	- utter_goodbye
	
## top 3 cases as per deceased
* greet
    - utter_greet 	
* top_world{"case_type": "deceased", "CARDINAL": "3"}
    - slot{"CARDINAL": "3"}
    - slot{"case_type": "deceased"}
    - action_top_world
* goodbye
	- utter_goodbye
