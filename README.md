# PyData NYC 2018 - Going beyond “Sorry, I didn’t get that”: building AI assistants that scale using machine learning

This repo contains the code for my workshop at PyData NYC 2018.

## Installation

To follow this demo, you will need Rasa NLU, Rasa Core and spacy installed. You can do it by running:


`python -m pip install -U rasa_core==0.11.11 rasa_nlu==0.13.6`

You will also need an additional one additional dependency:

`python -m pip install sklearn_crfsuite`


## How to use this repository

The repo contains three notebooks:
- `rasa-pydatanyc-workshop-starter` - this is a notebook which we will used during the workshop
- `rasa-pydatanyc-workshop-completed` - this is a notebook which contains the completed, not executed code of the workshop
- `rasa-pydatanyc-workshop-executed` - this is a notebook which contains the complete and executed code of the workshop

The additional files in this repo will be explained during the session. Once you train the models, you can find them in a directory called `models`.

## Get in touch

If you encounter any problems while installing the dependencies or have any questions regarding this notebook, shoot me a message on juste@rasa.com
