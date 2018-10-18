


## Suggestion path 1
* greet
  - utter_greet
* paper_search
  - utter_what_type
* inform{"paper_type":"machine learning"}
  - action_paper_search
  - utter_approve
* affirm
  - utter_send_link
* goodbye
  - utter_goodbye

## Suggestion path 2
* greet
  - utter_greet
* paper_search{"paper_type":"chatbots"}
  - action_paper_search
  - utter_approve
* affirm+authors
  - utter_send_link
  - utter_authors
* thanks
  - utter_happy_reading
* goodbye
  - utter_goodbye

## Suggestion path 3
* greet
  - utter_greet
* paper_search{"paper_type":"statistics"}
  - action_paper_search
  - utter_approve
* deny
  - utter_goodbye
  
## Suggestion path 4
* greet
  - utter_greet
* paper_search{"paper_type":"statistics"}
  - action_paper_search
  - utter_approve
* affirm
  - utter_send_link
* authors
  - utter_authors
* thanks
  - utter_happy_reading
* goodbye
  -utter_goodbye
  

## Suggestion path 5
* greet
  - utter_greet
* paper_search{"paper_type":"mathematics"}
  - action_paper_search
  - utter_approve
* authors
  - utter_authors
* send_link
  - utter_send_link
* goodbye
  -utter_goodbye
  
  
## Suggestion path 6
* greet
  - utter_greet
* paper_search
  - utter_what_type
* inform{"paper_type":"chatbots"}
  - action_paper_search
  - utter_approve
* authors
  - utter_authors
* send_link
  - utter_send_link
* thanks
  - utter_happy_reading
* goodbye
  -utter_goodbye 
  
  
## Suggestion path 7
* greet
  - utter_greet
* paper_search
  - utter_what_type
* inform{"paper_type":"chatbots"}
  - action_paper_search
  - utter_approve
* affirm+authors
  - utter_send_link
  - utter_authors
* thanks
  - utter_happy_reading
* goodbye
  -utter_goodbye 
  
  
## Suggestion path 8
* greet
  - utter_greet
* paper_search
  - utter_what_type
* inform{"paper_type":"statistics"}
  - action_paper_search
  - utter_approve
* affirm+authors
  - utter_send_link
  - utter_authors
* thanks
  - utter_happy_reading
* goodbye
  -utter_goodbye   


## Suggestion path 9
* greet
  - utter_greet
* paper_search{"paper_type":"physics"}
  - action_paper_search
  - utter_approve
* affirm
  - utter_send_link
* authors
  - utter_authors
* thanks
  - utter_happy_reading
* goodbye
  -utter_goodbye 

