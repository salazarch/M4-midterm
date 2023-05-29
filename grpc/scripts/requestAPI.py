## @file
# Script to retrieve Pokemon data from the PokeAPI and save it as a JSON file

import requests
import time
import json

## The endpoint representing the Pokemon
endpoint = "ditto"

## Make a request to the PokeAPI to retrieve Pokemon data
request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{endpoint}")

## Get the current timestamp
timestamp = str(time.time()).split(".")[0]

## Save the Pokemon data as a JSON file
with open(f"pokemon-{endpoint}-{timestamp}.json", "w") as file:
    file.write(json.dumps(request.json(), indent=4))
